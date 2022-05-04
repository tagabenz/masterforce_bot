FROM python:alpine
  WORKDIR app
  COPY . .
  RUN pip install -r requirements.txt
  ENTRYPOINT [ "python" ]
  CMD [ "start.py" ]
