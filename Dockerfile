FROM ubuntu

RUN apt update && \
    apt upgrade -y && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa

RUN apt install python3.10 -y
RUN apt install python3.10-venv -y
RUN ln -s /usr/bin/python3.10 /usr/bin/python
RUN apt install make

RUN mkdir /app
WORKDIR /app

CMD ["/bin/bash"]