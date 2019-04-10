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

 cal("yum update -y")
 cal("yum install nmap -y")
 cal("yum install git -y")
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

  cal("apt-get update -y")
  cal("apt-get install nmap -y")
  cal("apt-get install git -y")
  cal("mkdir files")
  cal("pip install sockets")
  cal("cd files && git clone https://github.com/dotfighter/torshammer")
  cal("cd files && git clone https://github.com/jseidl/GoldenEye")
  cal("cd files && git clone https://github.com/gkbrk/slowloris")
  cal("cd files && git clone https://github.com/thurties/udp")
  cal("clear")
  print("ALL FILES INSTALLED AND READY TO GO!")
