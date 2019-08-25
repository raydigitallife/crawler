From ubuntu
RUN apt-get update
RUN apt-get install python-pip -y
RUN pip install lxml wheel requests pandas beautifulsoup4

COPY demo.py demo2.py /

CMD [ "python","/demo2.py"]