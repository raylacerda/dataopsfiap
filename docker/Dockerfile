FROM ubuntu:latest

RUN apt-get update -y \
    && apt-get install zip -y \
    && apt-get install default-jre -y \
    && apt-get install sudo -y \
    && apt-get clean -y

COPY Aula1_2.zip /tmp

RUN cd /tmp/ \
    && unzip Aula1_2.zip \
    && cd Aula1 \
    && chmod +x Aula1_run.sh

ENTRYPOINT [ "sh", "/tmp/Aula1/Aula1_run.sh"]
