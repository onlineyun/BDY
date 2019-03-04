import requests
import json
import re

def get_content(url,data):
    headers = {
        'Connection': 'keep-alive',
        # 'Content-Length': '113',
        'Origin': 'chrome-extension://anlllmnpjodopgbkbpnghnjlelnogfjc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
    }

    response = requests.post(url,headers=headers,data=data)
    return response.json()
def search(sea_url):

    uuids = matchall(sea_url, ['pan.baidu.com/s/1([\w]+)'])

    if  uuids:
        data = {'uuids':'BDY-{}'.format(uuids[0]),
               'client_version':'2018.12'}
        req_url = 'https://ypsuperkey.meek.com.cn/api/v1/item/check-data'

        html = get_content(req_url,data)
        print(html)
    else:
        print("查询的url匹配不正确")

def matchall(text, patterns):
    """Scans through a string for substrings matched some patterns.

    Args:
        text: A string to be scanned.
        patterns: a list of regex pattern.

    Returns:
        a list if matched. empty if not.
    """

    ret = []
    for pattern in patterns:
        try:
            match = re.findall(pattern, text)
        except(TypeError):
            match = re.findall(pattern, str(text))
        ret += match

        if ret:
            return ret

    return None
if __name__ == '__main__':
    '''
    pan.baidu.com/s/1    
    '''
    url = 'pan.baidu.com/s/191xssKElUKt0d6zz0TgqpA'
    search(url)
