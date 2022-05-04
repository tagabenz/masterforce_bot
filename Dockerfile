FROM python:alpine
  WORKDIR app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  ENTRYPOINT [ "python" ]
  CMD [ "start.py" ]
