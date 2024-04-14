import os
import socket
#import nmap

z = os.getlogin()
print("Log In: " + z)
x = socket.gethostname()
print("Machine Name: " + x)
y = socket.gethostbyname(x)
print("IP Address: " + y)
i = 0
#prints ports
for port in range(65535):
    try:
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serv.bind((y,port))
    except:
        i = i + 1
        print("[Open] Port Open:",port)
    serv.close()
print("Open ports (total): " + str(i))
print("Closed ports (total): " + str(65535 - i))

q = socket.gethostbyaddr(y)
name = len(x)
net = q[0]
net = net[name:]
print("Network: " + net)
print(q)
#print(q)
'''
ninfo = getnameinfo
socket.getnameinfo(sockaddr, flags)
'''
prefix = "IPPROTO_"
table = {num:name[len(prefix):] 
          for name,num in vars(socket).items()
            if name.startswith(prefix)}

#shows protocols in the computer
assert table[6] == 'TCP'
assert table[0x11] == 'UDP'
print(len(table)) # in python 3.10.0 this has 30 entries
from pprint import pprint
pprint(table) # if you want to see what is available to you
'''
ip_proto={v:k[8:] for (k,v) in vars(socket).items() if k.startswith('IPPROTO')}
print(socket.getprotobyname(ip_proto))
'''
print("PUP exists at proto number: " + str(socket.getprotobyname("PUP")))
#establishes handshake between the two
'''
underlyingProtocol = "tcp"
serviceList = ["HOPOPTS", "ICMP", "IGMP", "GGP", "IPV4", "ST", "TCP", "CBT", "CBT", "EGP", "IGP", "PUP", "UDP", "IDP", "RDP", "IPV6"]
#print(serviceList)

for s in serviceList:
    portNum = socket.getservbyname(s,underlyingProtocol)
    print("The service " + s + " uses port number " + portNum)

#print(socket.getservbyname(17[, PUP]))
'''
#-------------------------------
'''
scan = nmap.PortScanner()
scan.scan(y, x)
scan.command_line()
'''
