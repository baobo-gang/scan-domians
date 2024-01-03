# coding=utf-8
import requests
from bs4 import BeautifulSoup
import queue
import threading
import sys
sys.path.append("..")
from config import *

que = queue.Queue()
gjc = f"site:{domain}"
url = f"https://www.google.com/search?q={gjc}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
domain_list = []
threads = []
path = "./domain.txt"


def jg():
    while not que.empty():
        page = que.get()
        try:
            params = {"q": gjc, "start": (page - 1) * 10}
            res = requests.get(url, headers=header, params=params)
            print(res.status_code)
            html = res.text
            soup = BeautifulSoup(html, "html.parser")
            text = soup.find_all("cite")
            for doman in text:
                domans = doman.text
                if "http" in domans or "https" in domans:
                    c_domans = domans.split("›")[0]
                    domain_list.append(c_domans)
        except Exception as e:
            pass


def main2():
    for page in range(1, pages + 1):
        que.put(page)

    for i in range(thread):
        t = threading.Thread(target=jg)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    dd = set(domain_list)
    with open(path, "a") as file:
        for d in dd:
            if "https" in d:
                file.write(d[8:] + "\n")
                print(d[8:])
            else:
                file.write(d[7:] + "\n")
                print(d[7:])

