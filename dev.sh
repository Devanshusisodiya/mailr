#!/bin/bash

# Kill existing processes on script exit
trap 'kill $(jobs -p) 2>/dev/null' EXIT

echo "Starting development servers..."

# Start Celery Worker
echo "Starting Celery Worker..."
uv run celery -A hermes.scheduler:celery_app worker --loglevel=info &

# Start Celery Beat
echo "Starting Celery Beat..."
uv run celery -A hermes.scheduler:celery_app beat --loglevel=info &

# Start FastAPI
echo "Starting FastAPI..."
uv run uvicorn hermes.main:app --reload &

# Wait for all background processes
wait