# stagearchiveunpack.py

import os

files = [f for f in os.listdir("stage3") if os.path.isfile(os.path.join("stage3", f))]

def stage3unpackchoise():

    def list_stage3_files():
        for i,file in enumerate(files, start=1):
            print(f"{i} {file}")
        return files

    def select():
        selection = int(input("\nEnter the number of the file you want to select: "))
        global selected_file
        selected_file = files[selection - 1]
        print(f"\nSelected file: {selected_file}")
    def unpack():
        os.system(f"tar xpvf stage3/{selected_file} -C /mnt/gentoo")

    list_stage3_files()
    select()
    unpack()
