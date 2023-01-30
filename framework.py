#!/usr/bin/env python3
# Coded by: AuxGrep
#           Sh3dyz
# 2023

import time, sys, os
from AP.alert import disclaimer
import platform

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

os_check = platform.system()

if os_check != 'Linux':
    sys.exit('Framework support On linux!!!')


def big_banner():
    print(f'''{grey}
                   ,▄▄▄▄▄╓,
				               ,,▄▄▄▄▓█████████████████████▓▓▄▄▄▄,,
	                 ▀▀████████████████████████████████████████▓▄▄▄▄▄▄▄,     
	                ▄▄██████████████████████████████████████████████▌▄╓▄∩
	             ▄██▀▀████████████████████████████████████████████████▄,     '
	            `   ▄█████████{pink}▓{grey}████{pink}▓▓▓▓▓▓▓▓▓{grey}███████{pink}▓{grey}██████▄▄L,
	              ▄██████████{pink}▓{grey}███{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}████{pink}▓{grey}███████▀
	             └▀╙ ▓██████{pink}▓{grey}██{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}███{pink}▓▓▓{grey}████▀╙`
	                ,███████{pink}▓{grey}██{pink}▓▓▓▓▓▓{grey}████{pink}▓▓▓▓▓▓▓▓▓{grey}██{pink}▓{grey}███
	                ▓██████████{pink}▓▓▓▓▓▓{grey}█████{pink}▓▓▓▓▓▓▓▓{grey}██{pink}▓{grey}█████m
	                ████████{pink}▓{grey}████{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}████████████████████,
	               J█████████{pink}▓{grey}████{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}███{pink}▓{grey}██████▀╙
	               ╟█████████████{pink}▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}████{pink}▓{grey}████████████████▀
	             {pink} ▄▓▓{grey}████████████{pink}▓▓▓{grey}█████████████████████████████████▀{pink}╨
	             Φ▌▓▓▓{grey}███████████████████████████████████████{pink}▓▓▓▓▌Å"`
	              ⌐'╫▓▓▓▓▓▓▓▓▓▓▓▓▓{grey}███████████████████████{pink}{END}▓▓▓▓▓▓▓Ñ`
	              `  "▌░╟╫╨╢║╣▀▓▓▓▀▀▀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌▀▀▀▀╣ÖÅ`╠░║▓:
	             `    ▌ "╫. j  ▓▓▒" ``╟╫M` ```└```     ╙⌂║. "Ñ▓▌ Developed By{red} Auxgrep{END} and{red} Sh3dYz{END}
	                 ▐M `╨H ¿ "▓▓╫    ╣Ñ      j         ╣╬   ║▓    {green}pew! pew!!{END}
	                 ╬   :Ñ"  ╫▓╣Ü    ╣░      j         ╙▌   ╣▌        2023

	                 ''')


def Menu():
    print('')
    HEAD = '{0}{3}{2}WELCOME TO DARK-EAGLE WIFI KIT LOADER v1{1}'.format(BOLD, END, red, ITALIC)
    size = HEAD.center(97)
    print(size)
    print('')
    print('Choose a module'.center(80))
    print('____'.center(70))
    print('')
    print(f'[1] AP-Sniffer {green}{BLINK}(✓){END}'.center(90))
    print(f'[2] Handshakes-sooper{green}{BLINK}(✓){END}'.center(95))
    print(f'[3] Deauthentication attack {green}{BLINK}(✓){END}'.center(101))
    print(f'[4] Monitor Mode{green}{BLINK}(✓){END}'.center(90))
    print(f'[5] MITM - ByPass Private Dns(IOS 16 and UP){green}{BLINK}(✓){END}'.center(117))
    print(f'[6] Manage Mode{green}{BLINK}(✓){END}'.center(90))
    print(f'[7] VIF-checking{green}{BLINK}(✓){END}'.center(90))
    print(f'[8] Strolling Attacks{green}{BLINK}(✓){END}'.center(95))
    print(f'{BOLD}[9]{blue}*** Refresh **** {END}{pink}{BLINK}ヽ(•‿•)ノ{END}'.center(115))
    print(f'[10] Evil-Twin Attacks-**SOON**{red}{BLINK}(x){END}'.center(105))
    print('')
    print(f'{red}[0] Exit {END}'.center(90))
    print('____'.center(70))
    print('')

    value = None  # INT VALUE TO BE RETURNED

    while True:
        try:
            module_number = input(f'{green}Enter module{END} {purple}ID(1-10){END}: ')
        except:
            sys.exit(f'{purple}Thanks for Your Time!! Byeee!!{END}'.center(100))
        try:
            module_number = int(module_number)
        except ValueError:
            print('Please choose module {0}number 1 to 10{1}'.format(red, END))
            continue

        if module_number == int(1):
            value = 1
            break
        elif module_number == int(2):
            value = 2
            break
        elif module_number == int(3):
            value = 3
            break
        elif module_number == int(4):
            value = 4
            break
        elif module_number == int(5):
            value = 5
            break
        elif module_number == int(6):
            value = 6
            break
        elif module_number == int(7):
            value = 7
            break
        elif module_number == int(8):
            value = 8
            break
        elif module_number == int(9):
            value = 9
            break
        elif module_number == int(10):
            value = 10
            break

        elif module_number == int(0):
            os.system('clear')
            sys.exit(f'{purple}Thanks for Your Time!! Byeee!!{END}'.center(100))
            
       
        else:
            print('Please choose module {0}number 1 to 5{1}'.format(red, END))
            continue
    # RETURN INT VALUE
    return value


big_banner()
disclaimer()
while True:
    try:
        module_number = Menu()  # CALL MENU THEN MENU WILL RETURN INT VALUE

        if module_number == int(1):
            os.system('clear')
            time.sleep(2)
            print('{0}LOADING AP-SNIFFER{1}'.format(green, END))
            print('')
            from bar.bar import bar_module2

            bar_module2();
            print('')
            time.sleep(3)
            print('')
            from AP.module import module1

            module1()
            time.sleep(2)
            os.system("clear")
        # LOOP BACK TO MENU

        elif module_number == int(2):
            os.system('clear')
            print('LOADING HANDSHAKE MODULE V1-BETA')
            from banner.banner import banner

            banner()
            from bar.bar import bar_module2

            bar_module2();
            from handshakes import module_handshakes

            time.sleep(2)
            os.system("clear")
        # LOOP BACK TO MENU

        elif module_number == int(3):
            os.system('clear')
            print('{0} LOADING DEAUTHENTICATION MODULE {1}'.format(green, END))
            print('')
            from bar.bar import bar_module2

            bar_module2();
            time.sleep(2)
            from AP.dds import *

            module_number()
            time.sleep(2)
            os.system("clear")
        # LOOP BACK TO MENU

        elif module_number == int(4):
            # LOOP BACK TO MENU
            os.system('clear')
            print('LOADING ......wait!!!')
            from bar.bar import bar_module2
            bar_module2()
            os.system('clear')
            from banner.banner import banner
            banner()
            from AP.monitor import monitor
            monitor()
            time.sleep(3)
            os.system("clear")

        elif module_number == int(5):
            os.system('clear')
            print('{0}LOADING MITM MODULE BYPASS IOS 16 AND UP{1}'.format(green, END))
            print('')
            from bar.bar import bar_module2

            bar_module2();
            time.sleep(2)
            from evilMITM.loader import moduleMitmf

            moduleMitmf();
            time.sleep(2)
            os.system("clear")
        elif module_number == int(6):
            os.system('clear')
            print('LOADING .........')
            from bar.bar import bar_module2
            bar_module2()
            os.system('clear')
            from banner.banner import banner
            banner()
            from AP.managed import interface_managed
            interface_managed()
            os.system('clear')

        elif module_number == int(7):
            os.system('clear')
            print('LOADING MODULE ......VIF-CHECKER')
            from bar.bar import bar_module2
            bar_module2()
            os.system('clear')
            from banner.banner import banner
            banner()
            from VIF.vif import VIF
            VIF()
            os.system('clear')
        
        elif module_number == int(8):
            os.system('clear')
            print('LOADING STROLLING MODULE!!')
            from bar.bar import bar_module2
            bar_module2()
            os.system('clear')
            from banner.banner import banner
            banner()
            from mk47.module import mk47
            mk47()
            os.system('clear')

        elif module_number == int(9):
            os.system('clear')
            print(f'{BOLD}{green}success!!{END} {BOLD}refreshed{END}'.center(120))
            dr = os.getcwd()
            from bar.refresh import refresh
            refresh()
        elif module_number == int(10):
            os.system('clear')
            print(f'{red}{BOLD}{ITALIC}{BLINK} Module 10, Still On development!! Try Again letter{END}')
            
        # LOOP BACK TO MENU
    except Exception as E:
        print(f"\nError Name: {E}")
        sys.exit(
            '\nUnkwown error !! OCCURED !! if you Think this is bug.\nGood report it here {0}{2}mranonymoustz@tutanota.com{1}'.format(
                red, \
                END, ITALIC))
