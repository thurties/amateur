import subprocess

def cal(cmd):
	subprocess.call(cmd, shell=True)

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
 cal("cd files && git clone https://github.com/gkbrk/slowloris")
 cal("cd files && git clone https://github.com/thurties/udp")
 cal("clear")
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
  cal("cd files && git clone https://github.com/gkbrk/slowloris")
  cal("cd files && git clone https://github.com/thurties/udp")
  cal("clear")
  print("ALL FILES INSTALLED AND READY TO GO!")
