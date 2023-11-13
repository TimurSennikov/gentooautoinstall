# commandnotfoundcheck.py
import os
import time
import math
import subprocess

commands_to_check = ["wipefs", "parted", "mkfs.vfat"]

for command in commands_to_check:
    command_check = subprocess.getoutput("command -v " + command)
    if command_check=="":
        print("Command '" + command + "' not found. Please install it and try again.")
        exit(1)
