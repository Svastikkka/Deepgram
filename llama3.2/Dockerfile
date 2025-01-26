FROM python:3.10-slim
WORKDIR /app
COPY app.py /app/app.py
RUN apt-get update && apt-get install -y \
    && pip install --no-cache-dir \
    streamlit \
    transformers \
    torch \
    accelerate
ENV HUGGINGFACE_TOKEN=MYTOKEN
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]