FROM python:latest
  RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
  WORKDIR /app
  COPY . .
  RUN pip install -r requirements.txt
  USER uwsgi
  CMD ["./cmd.sh"]
