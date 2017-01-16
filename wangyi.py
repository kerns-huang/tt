#!/usr/bin/env python
# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from bs4 import Tag
from requests import request


def stocklist():
    page = 0
    reportdate = 20160930
    sort = "reportdate"
    order = "desc"
    while True:
        r = requests.get(
            "http://quotes.money.163.com/data/caibao/yjyg_00.html?reportdate={0}&sort={1}&order={2}&page={3}".format(
                reportdate, sort, order, page))
        if (r.content is None):
            break
        soup = BeautifulSoup(r.content, "html.parser")
        stocks = soup.find(name="table", attrs={"class": "fn_cm_table", "id": "plate_performance"})
        for child in stocks.children:
            if isinstance(child, Tag):
                if (child.a is not None):
                    r = requests.get(child.a.get('href'))
                    soup = BeautifulSoup(r.content, "html.parser")
                    ul = soup.find(name="ul", attrs={"class": "main_menu"})
                    finanReport(ul.contents[5].a.get('href'))
        page += 1


def finanReport(href):  ##获取财务报表信息
    r = requests.get(baseUrl + href)
    print r.content


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    baseUrl = "http://quotes.money.163.com"
    stocklist()
