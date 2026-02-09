FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
RUN adduser --disabled-password --gecos '' flask
COPY --from=builder /usr/local /usr/local
COPY --chown=flask:flask app/ app/
COPY --chown=flask:flask README.md .
USER flask
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD ["curl", "-f", "http://localhost:5000/health"] || exit 1
CMD ["python", "-m", "app"]