# 根據網路上資料實作 demo.py

<https://www.jamleecute.com/python-web-crawler-beautifulsoup-%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2/>

## 產出安裝文件，主要用作在python的函式庫

pip freeze > requirements.txt   
但產出的並非都是需要的，而是套件相依性本身已經安裝的，但可當作參考價值

## 包裝 docker images

ubuntu-python27.dockerfile
ubuntu-python3.dockerfile

## 使用方式,python27

docker run `your-docker-images` python demo.py   
demo.py 要依附在 container 內   

## 使用方式,python3
docker run `your-docker-images` python3 demo.py   
demo.py 要依附在 container 內   