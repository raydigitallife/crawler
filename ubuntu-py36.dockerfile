From ubuntu
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install lxml wheel requests pandas beautifulsoup4 boto3

COPY demo.py demo2.py /

CMD [ "python3","/demo2.py"]