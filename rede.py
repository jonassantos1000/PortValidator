import socket
import requests
import json
import threading
import sys
from time import sleep
from datetime import datetime

def findExternalIp():
    request = requests.get("https://api.ipify.org/").text
    return request

def findLocalIp():
    ip_local = socket.gethostbyname(socket.gethostname())
    return ip_local

def testPort(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    sock.close()

    if result == 0:
        return 'Aberta'
    else:
        return 'Fechada'
    
def local (start,end):
    for porta in range(start,end,1):
        ipLocal=findLocalIp()
        local = testPort(ipLocal,porta)
        
        if(local=='Aberta'):   
            sys.stdout.write('*** - Porta local: '+str(porta)+ ' aberta - ***\n')
            sys.stdout.flush()
    
def externa(start,end):
    for porta in range(start,end,1):
        ipExterno=findExternalIp()
        externo = testPort(ipExterno,porta)
        
        if(externo=='Aberta'):
            sys.stdout.write('*** - Porta externa: '+str(porta)+ ' aberta - ***\n')
            sys.stdout.flush()
            
def start():
    inicio = datetime.today().strftime('%H:%M')
    print("Inicio da execução: "+inicio)
    n=2
    i=1
    while (n<4000):
        threading.Thread(target=local, args=(i,n)).start()
        threading.Thread(target=externa, args=(i,n)).start()
        i=n
        n=n+1
    fim = datetime.today().strftime('%H:%M')
    tempo= datetime.strptime(fim,'%H:%M')-datetime.strptime(inicio,'%H:%M')
    print("*** - Fim validação. Tempo: "+ str(tempo) + " - ***")

start()
   

