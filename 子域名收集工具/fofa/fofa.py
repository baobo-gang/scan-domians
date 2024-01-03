# coding=utf-8
import requests
import base64
import sys
sys.path.append("..")
from config import *

api = "https://fofa.info/api/v1/search/all"
yj = f'domain="{domain}"'
base64_domain = base64.b64encode(yj.encode()).decode()
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
url = f"{api}?email={email}&key={key}&qbase64={base64_domain}&size={max_size}"
res = requests.get(url, headers=header)
results = res.json()
path = "./domain.txt"

def main3():
    jgs = []
    for result in results['results']:
        if "https" in result[0]:
            https = result[0][8:]
            jgs.append(https)
        else:
            jgs.append(result[0])

    jgs = set(jgs)
    with open(path, "a") as file:
        for jg in jgs:
            file.write(jg+"\n")
            print(jg)
