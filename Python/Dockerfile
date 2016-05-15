FROM ubuntu
MAINTAINER tpotter
LABEL version="1.0" \
      description="A container that contains the basic Python development setup for the udplugin."

RUN apt-get update && apt-get install -y python3-pip wget
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python3
RUN pip3 install requests pytest-runner mock pytest
