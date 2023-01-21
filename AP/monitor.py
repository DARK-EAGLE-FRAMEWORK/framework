#!/usr/bin/env bash

import subprocess
import time
import sys
import os

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
BROWN = "\033[0;33m"

interface = os.listdir('/sys/class/net')

class monitor():
    ask = str(input(f'{purple}{BOLD}{ITALIC}Your Adapter supported by AirCrack-package(y/n):{END} ')).lower()
    try:
        if ask == str('yes') or ask == str('y'):
            time.sleep(2)
            os.system('clear')
            print(f'{purple}{BOLD}{ITALIC}CHOOSE INTERFACE TO PUT IN MONITOR MODE{END}-{red}AIRCRACK SUPPORTED ADAPTERS{END}')
            print('')
            for i in interface:
                time.sleep(0.1)
                print(f'-> {i}')
            print('')
            card_interface = str(input(f'{BOLD}{purple}Enter intarface name:{END} ')).lower()
            if card_interface in interface:

                cmd_monitor = subprocess.run(["airmon-ng", "start", card_interface], stderr=subprocess.DEVNULL, \
                    stdout=subprocess.DEVNULL)
                print('success!! interface {0} on monitor mode'.format(card_interface))
            else:
                os.system('clear')
                sys.exit(f'Invalid Interface {card_interface}')
        elif ask == str('no') or ask == str('n'):
            time.sleep(2)
            os.system('clear')
            print(f'{BOLD}{purple}{ITALIC}CHOOSE INTERFACE TO PUT IN MONITOR MODE{END}')
            for i in interface:
                time.sleep(0.2)
                print(f'-> {i}')
            print('')
            card_interface = str(input(f'{BOLD}{purple}Enter intarface name:{END} ')).lower()
            if card_interface in interface:
                cmd_manual = subprocess.run(["ifconfig", card_interface, "down"])
                cmd_manual2 = subprocess.run(["iwconfig", card_interface, "mode", "monitor"])
                cmd_manual3 = subprocess.run(["ifconfig", card_interface, "up"])
                os.system('clear')
                print('success!! interface {0} on monitor mode'.format(card_interface))
            else:
                os.system('clear')
                sys.exit(f'{red}{BOLD}{ITALIC}Invalid Interface {card_interface}{END}')
        else:
            sys.exit('Unkwown option chooses!!')
    except KeyboardInterrupt:
        sys.exit('cancelled by User!! Good Bye')



      
    
    

