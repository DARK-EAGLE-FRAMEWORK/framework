#!/usr/bin/bash
# module mitm - framework loader

BOLD="\033[01;01m"     # makini sana
RED="\033[01;31m"      # error na warning
GREEN="\033[01;32m"    # fucked
YELLOW="\033[01;33m"   # kichwa
RESET="\033[00m"

clear
check_file="moduleMITM.py"

sleep 0.7 && echo -e    " ======================================="
sleep 0.6 && echo -e  "=                                           ="
sleep 0.5 && echo -e  "=      $RED MITM MODULE V1 - FRAMEWORK$RESET="
sleep 0.2 && echo -e  "=           bYPass PRIVATE DNS FEAUTURE     ="
sleep 0.01 && echo -e "=                                           ="
sleep 0.00 && echo -e "   ======================================"
echo ""

if [[ $EUID -ne 0 ]];
then
    echo -e 'PLease run the framework as root'
    exit 2
fi

if [ -f "evilMITM/moduleMITM.py" ]
then
    read -p "PLease Enter subnet Ip to Scan connected target(eg: 192.168.1.0/24): " targetIPs
    sleep 2
    clear
    echo -e "******************|| MODULE STARTED ||******************************"
    
    sudo python3 evilMITM/moduleMITM.py -ip_range $targetIPs
else
    echo -e 'An Error occured file $check_file not found'
fi