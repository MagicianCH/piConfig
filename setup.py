import os

#souces.list
os.system('sudo cp /etc/apt/sources.list /etc/apt/sources.list~')
os.system('sudo cp sources.list /etc/apt/')
os.system('sudo apt-get update')
print("sources.list done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#apue
os.system('sudo apt-get install libbsd-dev')
os.system('cp -r apue/ /home/pi/')
os.system('cd /home/pi/apue/ && make')
os.system('sudo cp /home/pi/apue/include/apue.h /usr/include/')
os.system('sudo cp /home/pi/apue/lib/libapue.a /usr/local/lib/')
print("apue done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#wiring pi
os.system('cp -r wiringPi/ /home/pi/')
os.system('cd /home/pi/wiringPi/ && ./build')
print("wiringPi done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#rtc
os.system('sudo cp rtc/modules /etc/')
os.system('sudo cp /etc/rc.local /etc/rc.local.bak')
os.system('sudo cp rtc/rc.local /etc/rc.local')
print("rtc done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#vim
os.system('sudo apt-get install vim')
os.system('git clone https://github.com/skyman1991/.vim.git')
os.system('cd /home/pi/.vim && mv vimrc ../.vimrc')
print("vim done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#lxde-pi-rc.xml
os.system('cp shortkey/lxde-pi-rc.xml /home/pi/.config/openbox/')
print("shortkey done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
