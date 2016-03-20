FROM ubuntu
MAINTAINER tpotter
LABEL version="1.0" \
      description="A container for the test environment for the udplugin"

ADD . /home/dev/SlackUrbanDictionaryPlugin

WORKDIR /home/dev/SlackUrbanDictionaryPlugin

RUN apt-get update && \
    apt-get install -y python3-pip && \
    python3 setup.py install
