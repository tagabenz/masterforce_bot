FROM python:alpine
  WORKDIR app
  RUN pip install -r requirements.txt
  ENTRYPOINT [ "python" ]
  CMD [ "start.py" ]
