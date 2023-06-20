FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
