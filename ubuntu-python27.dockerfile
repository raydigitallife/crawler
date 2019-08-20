# 用於測試 python27抓取 ptt的資料
From ubuntu
RUN apt-get update
RUN apt-get install python-pip -y
RUN pip install lxml wheel requests pandas beautifulsoup4
RUN mkdir work

COPY demo.py /work

CMD [ "python","/work/demo.py"]