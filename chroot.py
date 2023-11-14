# chroot.py

import subprocess
import os
import time

def chroot():

    os.system("cp --dereference /etc/resolv.conf /mnt/gentoo/etc/")
    os.system("mount --types proc /proc /mnt/gentoo/proc ")
    os.system("mount --rbind /sys /mnt/gentoo/sys")
    os.system("mount --make-rslave /mnt/gentoo/sys")
    os.system("mount --rbind /dev /mnt/gentoo/dev")
    os.system("mount --make-rslave /mnt/gentoo/dev")
    os.system("mount --bind /run /mnt/gentoo/run")
    os.system("mount --make-slave /mnt/gentoo/run")
