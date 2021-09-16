FROM python:3.8

RUN apt-get update \
    && pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip \
    && pip install -i https://mirrors.aliyun.com/pypi/simple/ scrapy==2.5.0 beautifulsoup4==4.9.3

CMD scrapy crawl crawl_article

COPY ad_articles.json /home/mob/AD_project/ad_django
