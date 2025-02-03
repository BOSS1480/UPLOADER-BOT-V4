FROM python:3.9-slim

WORKDIR /app

# התקנת תלותיות מערכת
RUN apt-get update && \
    apt-get install -y ffmpeg jq python3-dev && \
    rm -rf /var/lib/apt/lists/*

# העתקת קובץ הדרישות והתקנתן
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת שאר הקבצים
COPY . .

# הגדרת הפורט
EXPOSE 8000

# הרצת הבוט
CMD ["python3", "bot.py"]
