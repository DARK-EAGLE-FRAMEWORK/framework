#!/usr/bin/env python3 
# Boring Written By AuxGREP


# ABOUT

# A virtual network interface (VIF) is an abstract virtualized representation of a computer network \
# interface that may or may not correspond directly to a network interface controller.
# In order to make this happen your external cards must have capabilities of becoming splited out
# into two interfaces, for example "wlan1mon" this can be split out into "wlan1" and "mon"
# so we are 89% expecting that after monitor mode fuction if your card turned to like "somethingMON"
# that card is supporting VIF fuctions, means can be split it out into "something" as first interface and "mon" as second interface
# REASON of spliting cards: TO enable the interfaces to perform two attacks at once i.e Deauthentication attack and Building Fake 
# access POINT. 
# 
# 
# 

ITALIC = "\033[3m"
purple = '\x1b[38;5;165m'
blue = '\x1b[38;5;33m'
red = '\x1b[38;5;196m'
green = '\x1b[38;5;118m'
grey = '\x1b[38;5;0m'
pink = '\x1b[38;5;199m'
END = "\033[0m"
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
BLINK = "\033[5m"


import os
import time
import subprocess
import sys

interface_list = os.listdir('/sys/class/net') #retrieving interface connected to your Box
possibilities = ['wlan0mon', 'wlan1mon', 'wlan2mon', 'wlan3mon'] # interface to check

class VIF():

    for interface_x in interface_list: # for loop to print connected interface
        print(f'{ITALIC}--> {interface_x}')
    print('')
    interface = str(input(f'{BOLD}{purple}{ITALIC}ENter interface name:{END} ')) # ask user to enter selected interface for checking
    os.system('clear')
    try:

        if interface in interface_list: # loop for preparing monitor mode fuction by Aircrack via airmon-ng
            cmd = subprocess.run(["airmon-ng", "start", interface], stderr=subprocess.DEVNULL, \
                stdout=subprocess.DEVNULL)
            time.sleep(2)

        else:
            sys.exit(f'{BOLD}{red}{ITALIC}The interface {END}{ITALIC}{interface}{red}{BOLD}{ITALIC} is Invalid{END}')
            
        interface_list2 = os.listdir('/sys/class/net') # u can use while loop but for easy understand to beginers lets use this
        for check in interface_list2: # ask Again user to select interface after monitor mode
            print(f'{ITALIC}--> {check}')
        print('')
        monitor_interface = str(input(f'{BOLD}{purple}{ITALIC}Enter monitor mode interface:{END} ')) # usr will see all connected interface and choose
        os.system('clear')
        print('WAIT.......'.center(100)) # asking to wait
        os.system('clear')
        if monitor_interface in possibilities: # here we going to check if a choosen monitormode interface is in our capabilities LIST 
            time.sleep(2)
            os.system('clear')
            print(f'{BOLD}{green}{ITALIC}Your adapter {purple}{interface}{END}{green}{BOLD}{ITALIC} support VIF and can be used in EvilTwin Attacks{END}') # IF TRUE u get this output
            cmd2 = subprocess.run(["airmon-ng", "stop", monitor_interface], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            time.sleep(3)
        else:
            time.sleep(2)
            sys.exit(f'{BOLD}{red}{ITALIC}Sorry Bro!! This is unsupported adapter!!{END}') #if FALse USER will get this message
    except OSError:
        sys.exit('Unkwown Error Occured!!')   

