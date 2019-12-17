import requests
from bs4 import BeautifulSoup,SoupStrainer
import os
import time

h={
	"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

beep= lambda x: os.system("echo -n '\a';sleep 0.3;" * x)

def f_searcher(a):
	c=0;
	prev=" "
	surl="http://www.makautexam.net"
	ress=requests.get(surl,headers=h)
	ss=BeautifulSoup(ress.content,'html.parser')
	for link in ss.find_all('a',href=True):
		if link.has_attr('href'):
			ss=link.text
			if(ss.find('Notice')!= -1 and ss.find('Examination')!=-1 and ss.find(a)!=-1):
				print("exam might have been posponed check online")
				beep(3)
				return True
	return False


print ("enter date in format dd/mm/yyyy")
aa=input()
while(True):
	if f_searcher(aa)==False :
		print("working")
	time.sleep(10)
