# setup.py
import os
import time
import math

def initial_setup():

    print ("Hello and welcome to gentooautoinstall")

    doprintlsblk=input ("Do you wish to print lsblk command for you to know drives names? (Y/N): ")

    if doprintlsblk=="Y":
        print (os.system("lsblk"))
        osinstalldrive=input ("What drive do you want to use for install? ")
    else:
        osinstalldrive=input ("What drive do you want to use for insall? ")

    osinstalldriveesp=osinstalldrive+"1"
    osinstalldriveswap=osinstalldrive+"2"
    osinstalldriveroot=osinstalldrive+"3"

    fstypetouse=input ("what fs type do you want to use? ")

    
    kerneltouse=input ("what kernel do you want to use: 1 - gentoo-sources 2 - gentoo-kernel 3 - gentoo-kernel-bin ")
    if kerneltouse not in ["1", "2", "3"]:
        while True:
            print("invalid kernel number")
            kerneltouse = input("what kernel do you want to use: 1 - gentoo-sources 2 - gentoo-kernel 3 - gentoo-kernel-bin ")
            if kerneltouse in ["1", "2", "3"]:
                break

    donotexitpartition=input ("WARNING! ALL DATA ON " + osinstalldrive + ' WILL BE LOST. TO CONTINUE ENTER "YES" WITH CAPITAL LETTERS ')

    if donotexitpartition!="YES":
        print ("you dont entered YES")
        exit(1)

    print ("check all of your information\n")
    print ("drive: " + osinstalldrive + " file system to use: " + fstypetouse + " kernel: " + kerneltouse)

    timer=5
    while timer!=0:
        print("partitioning the drive in")
        print (timer)
        print ("...")

        time.sleep(1)
        timer=timer-1

    return osinstalldrive, osinstalldriveesp, osinstalldriveroot, osinstalldriveswap, fstypetouse, kerneltouse
