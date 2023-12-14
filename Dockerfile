FROM python:3.10-slim

RUN apt -y update
RUN apt -y upgrade
RUN apt -y install libpq-dev python3-dev build-essential
RUN apt install -y ffmpeg libsm6 libxext6

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "uwsgi", \
"--http", "0.0.0.0:5000", \
"--wsgi-file", "run.py", \
"--callable", "app", \
"--processes", "1", "--threads", "2"]
