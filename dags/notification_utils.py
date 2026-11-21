import json
import logging
import os
from datetime import datetime, timezone

import requests

logger = logging.getLogger(__name__)

def _send(url, payload, channel_name):
    if not url:
        logger.info("%s webhook not configured; alert skipped.", channel_name)
        return False
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info("%s notification delivered; HTTP %s", channel_name, response.status_code)
        return True
    except requests.RequestException as exc:
        # Never log the webhook URL; it is a secret.
        logger.exception("%s notification delivery failed: %s", channel_name, exc)
        return False

def send_alert(message, severity="CRITICAL"):
    timestamp = datetime.now(timezone.utc).isoformat()
    slack_payload = {"text": f":rotating_light: *{severity} — PIPELINE ALERT*\n{message}\n_Time: {timestamp}_"}
    discord_payload = {"content": f"🚨 **{severity} — PIPELINE ALERT**\n{message}\nTime: {timestamp}"}
    results = {}
    results["slack"] = _send(os.getenv("SLACK_WEBHOOK_URL", ""), slack_payload, "Slack")
    results["discord"] = _send(os.getenv("DISCORD_WEBHOOK_URL", ""), discord_payload, "Discord")
    logger.info("Notification delivery results: %s", json.dumps(results))
    return results

def task_failure_callback(context):
    ti = context.get("ti")
    exception = context.get("exception")
    dag_id = getattr(ti, "dag_id", "unknown_dag")
    task_id = getattr(ti, "task_id", "unknown_task")
    run_id = getattr(ti, "run_id", "unknown_run")
    message = (
        f"DAG: `{dag_id}`\n"
        f"Task: `{task_id}`\n"
        f"Run: `{run_id}`\n"
        f"Error: `{str(exception)[:500]}`"
    )
    send_alert(message, "CRITICAL")

def task_retry_callback(context):
    ti = context.get("ti")
    send_alert(
        f"DAG: `{getattr(ti, 'dag_id', 'unknown')}`\n"
        f"Task: `{getattr(ti, 'task_id', 'unknown')}`\n"
        "Task is entering a retry attempt.",
        "WARNING",
    )

def dag_failure_callback(context):
    dag_run = context.get("dag_run")
    logger.error(
        "DAG failure event: dag_id=%s run_id=%s",
        getattr(dag_run, "dag_id", "unknown"),
        getattr(dag_run, "run_id", "unknown"),
    )
