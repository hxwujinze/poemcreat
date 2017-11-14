from urllib import request
from bs4 import BeautifulSoup as bs
import sys   
sys.setrecursionlimit(10000) 
f = open("poetry.txt", "a")

for js in range(601,901):
	for ns in range(1,130):
		try:
			resp = request.urlopen('http://www16.zzu.edu.cn/qtss/zzjpoem1.dll/viewoneshi?js='+('%03d'%js)+'&ns='+('%03d'%ns))
			data = resp.read().decode('gbk')
			soup = bs(data, 'html.parser')
			poem = soup.find_all('font',style='font-size: 20pt')	
			if poem:  
				for item in poem:   
					print(item.text,end=':',file = f)
					print(item.text)
				poem = soup.find_all('font',style='font-size: 16pt')
				for item in poem:   
					print(item.text,file = f)
			else:
				break
		except:
			print('a error at %d%d'%(js,ns))
			continue



'''
resp = request.urlopen('http://www16.zzu.edu.cn/qtss/zzjpoem1.dll/viewoneshi?js=127&ns=040')
data = resp.read().decode('gbk')
soup = bs(data, 'html.parser')   
poem = soup.find_all('font',color='#FF0000')

for item in poem:   
	print(item.text,end=':',file = f)
	print(item.text)
poem = soup.find_all('font',style='font-size: 16pt')
for item in poem:   
	print(item.text,file = f)

'''
'''
for ns in range(88,91):
	resp = request.urlopen('http://www16.zzu.edu.cn/qtss/zzjpoem1.dll/viewoneshi?js=225&ns='+('%03d'%ns))
	data = resp.read().decode('gbk')
	soup = bs(data, 'html.parser')   
	poem = soup.find_all('font',style='font-size: 20pt')
	for item in poem:   
		print(item.text,end=':',file = f)
		print(item.text)
	poem = soup.find_all('font',style='font-size: 16pt')
	for item in poem:   
		print(item.text,file = f)
'''