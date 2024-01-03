# coding=utf-8
from 字典 import dict
from fofa import fofa
from google import google
from 鹰图 import hunter

def qc():
    with open("./domain.txt", "r") as file:
        #  列表推导式的语法，表示对每一行进行处理
        lines = [line.strip() for line in file.readlines()]

    line = set(lines)

    with open("./domain.txt", "w") as file:
        for lin in line:
            file.write(lin+"\n")

if __name__ == '__main__':
    banner = """
    欢迎进入子域名收集大全
    输入0开启所有收集模式
    输入1 开启google、fofa等被动收集
    """
    print(banner)
    user_input = input("请输入：")
    list_input = list(map(int, user_input))
    if 1 in list_input:
        google.main2()
        fofa.main3()
        # hunter.main4()
        qc()
    if 0 in list_input:
        google.main2()
        fofa.main3()
        hunter.main4()
        dict.main1()
        print("--------------去重-------------")
        qc()

