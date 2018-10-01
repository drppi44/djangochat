FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangochat
WORKDIR /djangochat
ADD requirements.txt /djangochat/
RUN pip3 install -r requirements.txt
add . /project_code/
