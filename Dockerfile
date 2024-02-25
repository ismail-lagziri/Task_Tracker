FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV SERVER_HOST=0.0.0.0
ENV SERVER_PORT=8000

CMD ["uvicorn", "main:prediction_app", "--host", "${SERVER_HOST}", "--port", "${SERVER_PORT}"]

