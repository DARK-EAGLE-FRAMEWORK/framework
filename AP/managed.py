import os
import time
import sys
import subprocess

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

view = os.listdir('/sys/class/net')

class interface_managed():

    try:
        for i in view:
            time.sleep(0.1)
            print(f'[*] - {i}')
        print('')
        
        choice = str(input(f'{BOLD}{purple}Select Monitored mode interface:{END} '))
        if choice in view:
                subprocess.run(["airmon-ng", "stop", choice], stderr=subprocess.DEVNULL, \
                stdout=subprocess.DEVNULL)
                print('Success!!! Go back to MainMenu')
                time.sleep(3)
        else:
            os.system('clear')
            sys.exit(f'{ITALIC}{BOLD}{red}ERROR!!!{END}{BOLD}{ITALIC} Selected interface {red}{choice}{END} : Not attached in your machine')

    except OSError:
        sys.exit('An Error occured!! Exiting')