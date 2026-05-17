import os
import platform

def update_system():
    os.system("sudo apt update && sudo apt upgrade -y")

def clean_system():
    os.system("sudo apt autoremove -y && sudo apt autoclean -y")

def show_info():
    print(f"OS: {platform.system()}")
    print(f"Kernel Version: {platform.release()}")
    