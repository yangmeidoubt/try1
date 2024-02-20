import json

import requests
if __name__ == '__main__':
    #1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2.指定UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'
    }
    #3.参数处理
    word = input(('enter a word:'))
    data = {
        'kw':word
    }
    #4.请求发送
    response = requests.post(url=post_url, data=data,headers=headers)
    #5.获取相应数据
    dic_obj = response.json()
    print(dic_obj)

    #持久化存储
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    fp.close()
    print('over!!!')

