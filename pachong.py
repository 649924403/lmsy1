import os
import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
import yaml
import json
def getHTMLText(url):
    try:
        kv = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        }
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
        return r.text
    except:
        print("Get HTML Error!")
        return ''



def parse_HTML(HTML):
    reg = r'<meta name="description" content="(\n|.)*<title>'
    reg2 = r''
    try:
        match = re.search(reg, HTML)
        match = re.sub('<meta name="description" content="', 'text: "', match.group(0))
        match = re.sub('">', '"', match)
        match = re.sub('<title>', '', match)
        print(match)
        return match
    except:
        print('Parse HTML Error!')
        return ''

def write_yaml(text):
    with open(r'C:\Users\86158\Desktop\DeepKE-main\example\ner\standard\conf\predict.yaml', "w", encoding="utf-8") as f:
        print(text)
        yaml.dump(text, f, allow_unicode=True)

def main():

 with open(r"C:\Users\86158\Desktop\DeepKE-main\example\ner\standard\爬取人名.txt", 'r+',encoding="utf-8") as line:
    keyword ="方帅"
    # a = input("是否清空原本txt: y or n")
    # if a == y:
    #     line.truncate(0)
    # b = input()
    # keyword = str(line)
    # print(line)
    if keyword:
        url = 'https://baike.baidu.com/item/' + keyword
        HTML = getHTMLText(url)

        text = parse_HTML(HTML)
        write_yaml(text)
        os.system("python predict.py")
if __name__ == '__main__':

    main()


