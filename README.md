# Pipeline Monitoring Practicum

Repository ini berisi dokumentasi dan implementasi praktikum Pipeline Monitoring menggunakan Apache Airflow, Docker, dan sistem notifikasi Slack Webhook.

## Teknologi yang Digunakan

- Python
- Apache Airflow
- Docker & Docker Compose
- PostgreSQL
- Slack Incoming Webhook

## Struktur Repository

```text
pipeline-monitoring-practicum/
├── dags/
├── scripts/
├── data/
├── config/
├── plugins/
├── docs/
│   ├── screenshots/
│   └── laporan-praktikum.md
├── .env.example
├── .gitignore
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Persiapan Environment

1. Install Docker Desktop.
2. Pastikan Docker menggunakan backend WSL2.
3. Clone repository ini.
4. Masuk ke direktori project.
5. Salin `.env.example` menjadi `.env`.
6. Sesuaikan konfigurasi environment dan webhook secara lokal.

## Menjalankan Project

Jalankan perintah berikut:

```bash
docker compose up -d
```

Periksa container:

```bash
docker compose ps
```

Buka Apache Airflow melalui:

```text
http://localhost:8080
```

## Praktikum

Repository ini mencakup implementasi dan dokumentasi praktikum:

- Pipeline monitoring menggunakan Apache Airflow.
- Monitoring pipeline latency.
- Penanganan task failure dan retry.
- Pengukuran metrik pipeline.
- Integrasi notifikasi Slack Webhook.

## Dokumentasi dan Bukti Praktikum

Seluruh dokumentasi dan bukti screenshot tersedia di:

`docs/screenshots/`

Laporan praktikum tersedia di:

`docs/laporan-praktikum.md`

## Catatan Keamanan

File `.env` tidak disertakan dalam repository karena berisi konfigurasi rahasia, termasuk URL webhook. Gunakan `.env.example` sebagai template konfigurasi.

---

**Project:** Pipeline Monitoring Practicum  
**Platform:** Apache Airflow, Docker, Python, PostgreSQL, Slack
