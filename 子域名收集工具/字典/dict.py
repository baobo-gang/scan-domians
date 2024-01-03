# coding=utf-8
import socket
import queue
import threading
import sys
sys.path.append("..")
from config import *

# 构建文件的绝对路径
file_path = "./字典/a.txt"
path = "./domain.txt"

que = queue.Queue()
threads = []
ip_list = []
output_lock = threading.Lock()


def chongfu(ips):
    """
    返回泛解析ip
    :param ips:
    :return:
    """
    dict_ip = {}
    list_ip = []
    for ip in ips:
        dict_ip[ip] = dict_ip.get(ip, 0) + 1
    for key1, value in dict_ip.items():
        if value > 1:
            list_ip.append(key1)
    return list_ip


def jg():
    wen()
    while not que.empty():
        domain_list = que.get()
        for d in domain_list:
            domains = f"{d.rstrip()}.{domain}"
            try:
                ip_address = socket.gethostbyname(domains)
                ip_list.append(ip_address)
                with open(path, "a") as file:
                    if ip_address in chongfu(ip_list):
                        ip_list.remove(ip_address)
                    else:
                        with output_lock:
                            file.write(domains + "\n")
                            print(domains)
                    que.task_done()
            except Exception as e:
                pass


def wen():
    with open(f"{file_path}", "r") as file:
        lines = file.read().splitlines()
        file_len = len(lines)
        domain_num = file_len // thread
        for j in range(0, file_len, domain_num):
            g = lines[j: j + domain_num]
            que.put(g)


def main1():
    for i in range(1, thread + 1):
        t = threading.Thread(target=jg)
        threads.append(t)
        t.start()

    que.join()

    for t in threads:
        t.join()


