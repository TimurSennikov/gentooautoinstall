# mount.py

import os

def mount(osinstalldriveesp, osinstalldriveswap, osinstalldriveroot):
    os.system(f"mount {osinstalldriveroot} /mnt/gentoo")
    os.system(f"mount --mkdir {osinstalldriveesp} /mnt/gentoo/boot")
    os.system("cd /mnt/gentoo")
