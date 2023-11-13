# partitioning.py
import os
import time
import math
import subprocess

def partition_drive(osinstalldrive, osinstalldriveesp, osinstalldriveswap, osinstalldriveroot, fstypetouse):
    if not osinstalldrive.startswith("/dev/"):
        osinstalldrive="/dev/"+osinstalldrive
    
    osinstalldriveesp=osinstalldrive+"1"
    osinstalldriveswap=osinstalldrive+""
    osinstalldriveroot=osinstalldrive+"2"
    
    os.system("wipefs --all " + osinstalldrive)
    os.system("parted " + osinstalldrive + " mklabel gpt")
    os.system("parted -a optimal " + osinstalldrive + " mkpart primary 0% 5% set 1 esp")
    os.system ("parted -a optimal " + osinstalldrive + " mkpart primary 5% 100%")
    os.system ("mkfs.vfat -F 32 " + osinstalldriveesp)
    os.system ("mkfs." + fstypetouse + " " + osinstalldriveroot)
    if fstypetouse=="btrfs":
        os.system ("mkfs." + fstypetouse + " " + osinstalldriveroot + " -f")
