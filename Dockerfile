FROM python:alpine
  WORKDIR masterforce_bot
  COPY . .
  RUN pip install -r requirements.txt
  CMD ["python3","start.py"]
