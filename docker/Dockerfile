FROM python:3.11-slim

# apt update
RUN apt-get update && apt-get install -y --no-install-recommends curl

# uv インストール
RUN curl -LsSf https://astral.sh/uv/install.sh | sh