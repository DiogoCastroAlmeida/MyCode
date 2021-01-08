#Networking Tools with socket module

import socket
import colorama
from colorama import Fore, Style
import utilities_module

colorama.init(autoreset=True)

def get_service_by_port(port):
    try:
        service = socket.getservbyport(int(port))
        utilities_module.print_extra_line(f"Service for port {port}: {Fore.GREEN}{service}")
    except OverflowError:
        utilities_module.print_extra_line(f"{Fore.RED}ERROR{Style.RESET_ALL} Port number most be in range 0-65535")
    except OSError:
        utilities_module.print_extra_line(f"{Fore.RED}ERROR{Style.RESET_ALL} Service not found.")


#get_service_by_port("80")


def get_ipaddr(hostname, extended=False):
    #also supports for localhost and dns names
    try:
        addr = socket.gethostbyname_ex(hostname)
        if not extended:
            utilities_module.print_extra_line( f"IP addr for {hostname} is {Fore.GREEN}{addr[-1][0]}")
        elif extended:
            print(f"Alternative alias for {hostname}: {Fore.GREEN}{utilities_module.convert_empty_list_to_none(addr[1])}")
            utilities_module.print_extra_line(f"IP Addresses for {hostname}: {Fore.GREEN}{addr[-1]}")
    except socket.gaierror:
        utilities_module.print_extra_line(f"{Fore.RED}ERROR{Style.RESET_ALL} Couldn't get hostname for {hostname}")

get_ipaddr("Diogo",True)


def get_my_hostname():
    utilities_module.print_extra_line(f"This machine's hostname is {Fore.GREEN}{socket.gethostname()}")

#get_my_hostname()


def get_hostname(ip_addr, extended=False):
    try:
        dn = socket.gethostbyaddr(ip_addr)
        if not extended:
            utilities_module.print_extra_line(f"Hostanme for {ip_addr} is {Fore.GREEN}{dn[0]}")
        elif extended:
            print(f"Hostname for {ip_addr}: {Fore.GREEN}{dn[0]}")
            print(f"Alternative hostnames alias for {ip_addr}: {Fore.GREEN}{utilities_module.convert_empty_list_to_none(dn[1])}")
            utilities_module.print_extra_line(f"Alternative IP Addresses for {ip_addr}: {Fore.GREEN}{dn[2].remove(ip_addr)}")
    except socket.herror:
        utilities_module.print_extra_line(f"{Fore.RED}ERROR{Style.RESET_ALL} Host not found.")
    except socket.gaierror:
        utilities_module.print_extra_line(f"{Fore.RED}ERROR{Style.RESET_ALL} Invalid IP Address format.")



#get_hostname("192.168.1.131", True)


def get_port_by_service(name):
    try:
        port = socket.getservbyname(name)
        utilities_module.print_extra_line(f"Port for service{name}: {Fore.GREEN}{port}")
    except OSError:
        utilities_module.print_extra_line(f"{Fore.RED}ERROR{Style.RESET_ALL} Service not found.")

#get_port_by_service("tfyf")
