# 用於測試 python3抓取 ptt的資料
From ubuntu
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install lxml wheel requests pandas beautifulsoup4 boto3
RUN mkdir work

COPY demo.py /work

CMD [ "python3","/work/demo.py"]