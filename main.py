# main.py
from setup import initial_setup
from partitioning import partition_drive
from install import install
from stagearchiveunpack import stage3unpackchoise
from prechrootconfigure import makefileconfigure
from chroot import chroot
from emergestartsetup import startsetupemerge
from postchrootconfigure import genenlocale
osinstalldrive, osinstalldriveswap, osinstalldriveesp, osinstalldriveroot, fstypetouse, kerneltouse = initial_setup()
partition_drive(osinstalldrive, osinstalldriveesp, osinstalldriveswap, osinstalldriveroot, fstypetouse)
stage3unpackchoise()
makefileconfigure()
chroot()
startsetupemerge()
genenlocale()
