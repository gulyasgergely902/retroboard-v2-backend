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

EXPOSE 5000

WORKDIR /app/src

CMD ["python", "run.py"]

