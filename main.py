# main.py
from setup import initial_setup
from partitioning import partition_drive
from install import install

osinstalldrive, osinstalldriveswap, osinstalldriveesp, osinstalldriveroot, fstypetouse, kerneltouse = initial_setup()
partition_drive(osinstalldrive, osinstalldriveesp, osinstalldriveswap, osinstalldriveroot, fstypetouse)
install()
