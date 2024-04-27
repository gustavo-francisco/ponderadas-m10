FROM python:3.8-slim

WORKDIR /app

COPY app.py requirements.txt static/swagger.yaml static/Insomnia_2024-04-24.json ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
