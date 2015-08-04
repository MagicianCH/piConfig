import os

#souces.list
os.system('rm /etc/apt/sources.list')
os.system('touch /etc/apt/sources.list')
f = open(r'/etc/apt/sources.list','r+')
f.write("deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ wheezy main contrib no-free rpi")
f.close()
os.system('sudo apt-get update')

#apue
os.system('sudo apt-get install libbsd-dev')
os.system('cp -r apue/ ~/')
os.system('cd ~/apue/ && make')
os.system('sudo cp ./apue/include/apue.h /usr/include/')
os.system('sudo cp ./apue/lib/libapue.a /usr/local/lib/')

#wiring pi
os.system('cp -r wiringPi/ ~/.')
os.system('~/wiringPi/build')

#rtc
f = open(r'/etc/modules','a+')
f.write('i2c-bcm2708\ni2c-dev')
f.close()
os.system('sudo cp /etc/rc.local /etc/rc.local.bak')
os.system('sudo cp rc.local /etc/rc.local')
