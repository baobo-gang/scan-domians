# coding=utf-8
import base64
import requests
import json
import sys
sys.path.append("..")
from config import *


search = f'domain={domain}'
search = base64.urlsafe_b64encode(search.encode("utf-8")).decode()
path = "./domain.txt"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
url = f"https://hunter.qianxin.com/openApi/search?api-key={api_key}&search={search}&page=1&page_size={size}&is_web=1"

request = requests.get(url, headers=header)
html = request.text
htmls = json.loads(html)
urls = htmls["data"]["arr"]

def main4():
    with open(path, "a") as file:
        for url in urls:
            if "https" in url["url"]:
                file.write(url["url"][8:]+"\n")
                print(url["url"][8:])
            else:
                file.write(url["url"][7:]+"\n")
                print(url["url"][7:])
