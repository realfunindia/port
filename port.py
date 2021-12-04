import socket from IPy import IP from termcolor import colored

def scan(target): converted_ip = check_ip(target) print('\n' + '[-_0 Scaning Target] ' + str(target))

for port in range(20,500):
    port_scaner(converted_ip, port)
def check_ip(ip): try: IP(ip) return(ip) except ValueError: return socket.gethostbyname(ip)

def get_banner(s): return s.recv(1024)

def port_scaner(ipaddress, port): try: socke = socket.socket() socke.settimeout(0.4) socke.connect((ipaddress, port)) try:

        banner = get_banner(socke)
        print('[+] port ' + str(port) + ' :' + str(banner.decode().strip('\n')))
    except:
        print('[+] open Port '+ str(port))
except:
    pass
if name == "main": targets = input('[+] Enter targets To Scan(split multiple targets with,): ') if ',' in targets: for ip_add in targets.split(','): scan(ip_add.strip(' ')) else: scan(targets)
