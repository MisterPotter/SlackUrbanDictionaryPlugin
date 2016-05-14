FROM python3_udplugin
MAINTAINER tpotter
LABEL version="1.0" \
      description="A container for the test environment for the udplugin"

ADD . /home/dev/SlackUrbanDictionaryPlugin

WORKDIR /home/dev/SlackUrbanDictionaryPlugin

RUN python3 setup.py install
