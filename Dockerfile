FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask requests gTTS googletrans==4.0.0-rc1
RUN apt update && apt-get install -y espeak
EXPOSE 30080
ENTRYPOINT ["python", "example1.py"]
