import re
str=input('Please enter a IP address\n')
ipv4=str.split(".")
ipv6=str.split(":")

ipv4_len=0
ipv6_len=0

ipv4_len=len(ipv4)
ipv6_len=len(ipv6)

if(ipv6_len==0 and ipv4_len>0):
    check1=0
    for i in ipv4:
        if(0<=int(i)<=255):
            check1=1
        else:
            check1=0
elif(ipv4_len<4 and ipv6_len==8):
    check2=0
    for i in ipv6:
        if(re.match(r'^[0-9a-fA-F]+$', i)):
            check2=1
        elif(i.isdigit()):
            check2=1
        else:
            check2=0
else:
    check1=0
    check2=0

if(ipv4_len==4 and check1==1):
    print('IPv4')
elif(ipv6_len==8 and check2==1):
    print('IPv6')
else:
    print('Neither')
