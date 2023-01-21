#!/usr/bin/bash
# setup


if [[ $EUID -ne 0 ]];
then
    echo -e 'PLease run the installation script as root'
    exit 2
fi

check_framework_file='framework.py'

if [ -f "framework.py" ]
then
    echo -e "[1] UPDATING YOUR SYSTEM"
    sudo apt-get update > /dev/null
    
    echo -e "[2] UPGRADING SOME PACKAGES"
    sudo apt-get upgrade > /dev/null
   
    echo -e "[3] INSTALLING PYTHON3 & PIP"
    sudo apt-get install python3 -y > /dev/null
    sudo apt-get install python3-pip -y > /dev/null
   
    echo -e "[4] INSTALLING AIRCRACK-PACKAGE"
    sudo apt-get install aircrack-ng -y > /dev/null

    echo -e "[5] INSTALLING PYTHON-TK"
    sudo apt-get install python3-tk -y > /dev/null

    echo -e "[6] INSTALLING PRETTYTABLE"
    sudo pip3 install prettytable > /dev/null

    echo -e "[7] INSTALLING IPADDRESS PACKAGE"
    sudo pip3 install ipaddress > /dev/null

    echo -e "[8] INSTALLING SCAPY NETWORK-LAYERS + MODULE"
    sudo pip3 install scapy > /dev/null

    echo -e "[9] INSTALLING tqdm"
    sudo pip3 install tqdm > /dev/null

    echo -e "[10] INSTALLING REQUESTS"
    sudo pip3 install requests > /dev/null

    echo -e "[11] INSTALLING DNSMASQ"
    sudo apt-get install dnsmasq -y > /dev/null

    echo -e "[12] INSTALLING WIRESHARK"
    sudo apt-get install wireshark -y > /dev/null

    echo -e "[13] INSTALLING HOSTAPD"
    sudo apt-get install hostapd -y > /dev/null

    echo -e "[14] INSTALLING SCREEN"
    sudo apt-get install screen -y > /dev/null

    echo -e "[15] INSTALLING WONDERSHAPER"
    sudo apt-get install wondershaper -y > /dev/null

    echo -e "[16] INSTALLING DRIFTNET"
    sudo apt-get install driftnet -y > /dev/null

    echo -e "[17] INSTALLING PYTHON DEV-TOOLS"
    sudo apt-get install python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg62-turbo-dev zlib1g-dev -y > /dev/null

    echo -e "[18] INSTALLING ADD PYTHON DEV TOOLS"
    sudo apt-get install libpcap-dev -y > /dev/null

    echo -e '[19] INSTALLING MITMPROXY'
    sudo python3 -m pip install mitmproxy > /dev/null

    echo -e "[20] INSTALLING DNSPYTHON"
    sudo python -m pip install dnspython > /dev/null

    echo -e "[21] INSTALLING PCAPY"
    sudo python -m pip install pcapy > /dev/null

    echo -e "[22] INSTALLING TWISTED"
    sudo python -m pip install twisted > /dev/null

    echo -e "[23] INSTALLING MDK4"
    sudo apt-get install mdk4 > /dev/null

    clear

    echo -e "SUCCESS!!!!! RUN THE FRAMEWORK NOW!"
else
    echo -e 'An Error occured file $check_framework_file not found'
fi