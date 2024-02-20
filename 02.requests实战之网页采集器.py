import requests
if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
    }
    url = 'https://sogou.com/web'
    #处理url所携带的参数
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    response = requests.get(url=url, params=param,headers=headers)

    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')