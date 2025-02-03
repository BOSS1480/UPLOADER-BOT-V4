FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y ffmpeg jq python3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN python3 -m pip check yt-dlp

CMD ["python3", "bot.py"]
