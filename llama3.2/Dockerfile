FROM python:3.10-slim
WORKDIR /app
COPY app.py /app/app.py
RUN apt-get update && apt-get install -y
RUN pip install --no-cache-dir \
    streamlit \
    transformers \
    torch \
    accelerate
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]