FROM --platform=linux/amd64 python:3.10-buster as build
ENV MODEL_NAME="Team-ACE/ToolACE-8B"
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY script.py .
CMD ["python", "script.py"]
