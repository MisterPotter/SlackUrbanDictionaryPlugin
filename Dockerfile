FROM python3_udplugin
MAINTAINER tpotter
LABEL version="1.0" \
      description="A container for the test environment for the udplugin"

ADD . /home/dev/SlackUrbanDictionaryPlugin

WORKDIR /home/dev/SlackUrbanDictionaryPlugin

# use pytest and install to save time whiile constantly running unit tests
RUN python3 setup.py install && python3 setup.py pytest

ENTRYPOINT ["python3", "src/udplugin/server.py"]
