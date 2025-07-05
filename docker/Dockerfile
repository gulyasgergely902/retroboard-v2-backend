FROM node:20-alpine AS builder

RUN npm install -g pnpm

WORKDIR /app

COPY frontend/ ./frontend
COPY src/ ./src
COPY build_frontend.sh ./

RUN chmod +x build_frontend.sh && \
    ./build_frontend.sh

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN python -m venv venv

ENV PATH="/app/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

COPY --from=builder /app/src/ ./src

WORKDIR /app/src

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "run:app"]
