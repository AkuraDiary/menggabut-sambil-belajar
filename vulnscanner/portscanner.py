import socket
from IPy import IP


class PortScan():
    banners = []
    open_ports = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num


    def scan(self):
        #converted_ip = check_ip(target)
        #print("\n" + '[-_0 scanning Target] '+ str(target))
        for port in range(1, self.port_num):
            self.scan_port(port)


    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target) #convert the domain name into ip addres

#    def get_banner(self):
#        return s.recv(1024)


    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip("\n").strip("\r")
                self.banners.append(banner)
                #print("[+] Open port "+ str(port)+ " : " + str(banner))
            except:
                #print("[+] Open port " + str(port))
                self.banners.append(" ")
            sock.close()
        except:
            #print("[-] Port "+ str(port) +" Is Closed")
            pass




'''
if __name__ == "__main__": # to prevent this code from executing if the file is imported
    targets = input('[+] Enter Target/s To Scan (split multiple targets with ,) : ')
    #converted_ip = check_ip(ipaddres)
    # # checking for multiple and single targets #
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
'''
