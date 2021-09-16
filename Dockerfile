FROM python:3.8

RUN pip install scrapy==2.5.0 beautifulsoup4==4.9.3 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

CMD scrapy crawl crawl_article

COPY ad_articles.json /home/mob/AD_project/ad_django
