FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps (kept minimal). Add build-essential if you need to build packages.
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy app
COPY . /app

EXPOSE 5000

# Use PORT env var provided by Render, fallback to 5000
CMD gunicorn app:app --bind 0.0.0.0:${PORT:-5000}
