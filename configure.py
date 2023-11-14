# configure.py

import os

def makefileconfigure():
    useflagstoadd=input("what use flags do you want to add? (if you want to skip this step, leave the field blank) ")
    os.system("rm /mnt/gentoo/etc/portage/make.conf")
    os.system('echo COMMON_FLAGS="-march=native -O2 -pipe" >> /mnt/gentoo/etc/portage/make.conf')
    os.system('echo CFLAGS="${COMMON_FLAGS}" >> /mnt/gentoo/etc/portage/make.conf')
    os.system('echo CXXFLAGS="${COMMON_FLAGS}" >> /mnt/gentoo/etc/portage/make.conf')
    os.system(f'echo USE="{useflagstoadd}" >> /mnt/gentoo/etc/portage/make.conf')
