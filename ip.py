import socket
import requests
import re 
myIP=socket.gethostbyname(socket.gethostname())
print(myIP)
myIP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myIP.connect(("www.naver.com",443))
print(myIP.getsockname()[0])

URL='http://ipconfig.kr'
response=requests.get(URL) 
#print(response.text)
myIP_1=re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', response.text)[1]
print(myIP_1) #외부 IP를 볼 수 있다.


