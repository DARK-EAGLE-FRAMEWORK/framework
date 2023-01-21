import sys
import os
import requests
from time import sleep

colorcode = {

    'ITALIC':'\033[3m', 'YELLOW':'\033[1;33m',
    'GREEN':'\033[0;32m', 'BLINK':'\033[5m',
    'RESET':'\033[0m', 'RED':'\033[0;31m',
    'BROWN':'\033[0;33m', 'PURPLE':'\033[0;35m',
    'ULINE':'\033[4m'

}

class disclaimer():
    def __init__(self):
        ujumbe = '\n\t{0}{5}{6}{4}{2}\n\x20\x20\x20{3}Hey Friend !! before starting using this program, Dont forget \
        \n\x20\x20\x20\x20\x20{0}{3}Hacking{2}{3} with out authorization is illegal, Dont use this program to attack\
            \n\t{3}networks with out legal permission, {1}{3}AuxGrep and Sh3dyz {2}{3} are not responsible with \
            \n\t\x20\x20{3}any {0}{3}malicious activities{2}\n'.format(colorcode['RED'], \
                colorcode['YELLOW'], colorcode['RESET'], colorcode['ITALIC'], "disclaimer".upper(), colorcode['ULINE'], colorcode['BLINK'])
        for unyama in ujumbe:
            print(unyama, end='', flush=True)
            sleep(0.01)
        print('')
        
        try:
            oky = str(input('{0}I Agree(yes/no):{1} '.format(colorcode['GREEN'], colorcode['RESET'])))
        except KeyboardInterrupt:
            sys.exit("\n\n{}Simply, just YES to agree or NO to decline!{}".format(colorcode['RED'], colorcode['RESET']))
        
        if oky.lower() in ["yes", "y"]:
            try:
                site = requests.get("http://net.lethack.tk", timeout=3, headers={"User-Agent":"{}".format(os.uname()[1])})
                os.system("clear")
            except:
                os.system("clear")

        else:
            os.system('clear')
            sys.exit('{0}Stupid dumbest KID!! Exiting....!!!{1}'.format(colorcode['RED'], \
                colorcode['RESET']))
