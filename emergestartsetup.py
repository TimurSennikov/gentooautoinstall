# emergestartsetup.py

import os
import time
import math

def startsetupemerge():
    os.chroot("/mnt/gentoo")
    os.chdir("/")
    os.system("emerge-webrsync")
    print("you will now be prompted to choose emerge profile. Please choose carefully. Check gentoo wiki for more info ")
    time.sleep(1)
    os.system("eselect profile list")
    profiletoselect=input("enter a number of profile you want to select ")
    os.system(f"eselect profile set {profiletoselect}")
    print("Updating @world set. It may take some time. See gentoo handbook for more details")
    time.sleep(1)
    os.system("emerge --ask --verbose --update --deep --newuse @world")
