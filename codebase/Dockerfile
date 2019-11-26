FROM ubuntu
RUN apt-get update
RUN apt-get install -y python-pip
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
