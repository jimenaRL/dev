FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y icecast2 ices2 && rm -rf /var/lib/apt/lists/*

ADD ./stream /stream
ADD . /app

RUN mkdir -p /var/log/ices/  &&  chmod 777 /var/log/ices/ && chown -R icecast2.icecast /app

USER icecast2
WORKDIR /app


# docker build -t espaces_imaginaire:latest .
# docker run -it --rm  -p 8000:8000 --name icecast2 -v /etc/localtime:/etc/localtime:ro espaces_imaginaire:latest bash -c "icecast2 -c icecast2_config.xml"
# docker run -it --rm --link icecast2:icecast2 espaces_imaginaire:latest bash -c "ices2 ices2_config.xml"