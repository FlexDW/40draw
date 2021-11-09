FROM continuumio/anaconda3:2021.05
RUN apt-get -y update --fix-missing &&\
  apt-get -y install python3-pip &&\
  pip install dash==1.21.0
COPY . /40draw5
WORKDIR /40draw5
ENTRYPOINT ["python", "app.py"]

