#!/usr/bin/env bash
set -e
sudo service docker start || true
echo "Waiting for Docker..."
for i in {1..20}; do
  if docker info >/dev/null 2>&1; then break; fi
  sleep 1
done
mkdir -p dags logs plugins config
echo "AIRFLOW_UID=$(id -u)" > .env
docker compose up airflow-init
docker compose up -d
echo "✅ Airflow is starting. Open port 8080."