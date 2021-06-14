import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print("\n" + '[-_0 scanning Target] '+ str(target))
    for port in range(1, 200):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(IP)
    except ValueError:
        return socket.gethostbyname(ip) #convert the domain name into ip addres

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddres, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddres, port))
        try:
            banner = get_banner(sock)
            print("[+] Open port "+ str(port)+ " : " + str(banner.decode().strip('\n')))
        except:
            print("[+] Open port " + str(port))
    except:
        #print("[-] Port "+ str(port) +" Is Closed")
        pass


if __name__ == "__main__": # to prevent this code from executing if the file is imported
    targets = input('[+] Enter Target/s To Scan (split multiple targets with ,) : ')
    #converted_ip = check_ip(ipaddres)
    # # checking for multiple and single targets #
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)

