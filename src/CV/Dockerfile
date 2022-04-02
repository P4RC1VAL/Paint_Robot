FROM ubuntu:latest

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


WORKDIR /home/p4rc1val/src

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip && apt-get install -y python3-opencv

COPY requirements.txt /src/requirements.txt
RUN pip3 install opencv-python

COPY CV.py /home/p4rc1val/src/CV.py
CMD python3 CV.py
