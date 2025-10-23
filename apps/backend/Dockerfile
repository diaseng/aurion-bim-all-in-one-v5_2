
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1     PIP_NO_CACHE_DIR=1     PIP_DISABLE_PIP_VERSION_CHECK=1
COPY requirements.txt .
RUN apt-get update &&     apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev curl &&     pip install --upgrade pip &&     pip install --no-cache-dir -r requirements.txt &&     apt-get purge -y build-essential &&     apt-get autoremove -y &&     rm -rf /var/lib/apt/lists/*
COPY . .
ENV PORT=10000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3   CMD curl -fsS http://localhost:10000/health/ready || exit 1
CMD ["bash","/app/entrypoint.sh"]
