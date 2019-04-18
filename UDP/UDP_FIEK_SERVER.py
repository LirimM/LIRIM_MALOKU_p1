from socket import *
import sys
from _thread import start_new_thread
import random
import datetime
import math

serverName='localhost'
#percaktojme portin e serverit
serverPort=12000

#krijimi i socketit me UDP(SOCK_DGRAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)

#socketit i rezervohet porti 12000
serverSocket.bind((serverName, serverPort))
print("Serveri FIEK_UDP eshte startuar..."+"\nServeri eshte i gatshem te pranoje kerkesa!\n")

global IPADRESA,NUMRIIPORTIT,BASHKETINGELLORE,PRINTIMI,EMRIIKOMPJUTERIT,KOHA,LOJA,FIBONACCI,KONVERTIMI,NRTEKST,MATH,find,findtwo,findthree,gabim,switch

gabim="Gabim!"

def findthree(arg,arg1,arg2):
   if arg in switch:
    try:
     y=switch.get(arg)
     z=y(arg1,arg2)
     return z
    except:
     z="Gabim!"
     return z.encode()

def findtwo(arg,arg1):
   if arg in switch:
    try:
     y=switch.get(arg)
     z=y(arg1)
     return z
    except:
     z="Gabim!"
     return z.encode()

def find(arg):
  try:
   if arg in switch:
     y=switch.get(arg)
   z=y()
   return z
  except:
   teksti="Gabim!"
   return teksti.encode()

#funksioni per percaktimin dhe kthimin e IP ADDRESS se klientit ne forme dhjetore psh (8.8.8.8)
def IPADRESA():
    ip=address[0]
    teksti = "IP Address-a e klientit eshte: "+str(ip)
    return teksti.encode()

#funksioni per percaktimin dhe kthimin e portit te klientit
def NUMRIIPORTIT():
        port=address[1]
        teksti="Porti i klientit eshte: "+str(port)
        return teksti.encode()

#funksioni per gjetjen e numrit te bashketingelloreve ne tekst dhe shfaqjen e ketij nr 
def BASHKETINGELLORE(text):
    fjala=str(text)
    string=fjala.strip()
    bashketingelloret = set ("BCDFGHJKLMNPQRSTVXZWbcdfghjklmnpqrstvxzw")
    try:

            if not string:
                return gabim.encode()
            else:
                nr=0
                for char in string: #kontrollojme cdo character ne string
                    if char in bashketingelloret: #nese characteri gjendet tek bashketingelloret pra rritet count
                        nr += 1

                teksti="Teksti permban "+str(nr)+" bashketingellore."
                return teksti.encode()
    except:
        return gabim.encode()

#funksioni per kthimin e fjalise se shtypur nga klienti
def PRINTIMI(f):
    t=str(f)    
    teksti = t.strip()
    if not teksti:
        return gabim.encode()
    else:
        return teksti.encode()

#funksioni per gjetjen dhe shfaqjen e emrit te kompjuterit te klientit
def EMRIIKOMPJUTERIT():
 try:
    h=gethostname()
    teksti=str(h)
    return teksti.encode()
 except:
     teksti="Emri i kompjuterit nuk u gjet!"
     return teksti.encode()

#funksioni per percaktimin e kohes aktuale ne SERVER dhe shfaqjen e saj te klienti ne nje format te lexueshem yy//mm/dd
def KOHA():
    now = datetime.datetime.now()
    teksti=now.strftime("%Y-%m-%d %H:%M:%S")
    return teksti.encode()
    
#funksioni per shfaqjen e 7 numrave te rastesishem nga rangu [1,49]
def LOJA():
    numrat="("
    for i in range(0,7):
        if i==6:
          numrat=numrat+str(random.randint(1,49))+")"
        else:
          numrat=numrat+str(random.randint(1,49))+","
    return numrat.encode()

#funksioni per llogaritjen dhe shfaqjen e numrit FIBONACCI te parametrit hyres
def LLOGFIBONACCI(l):
    n=int(l)
    if n == 0: return 0
    elif n == 1: return 1
    else: return (LLOGFIBONACCI(n-1)+LLOGFIBONACCI(n-2))

def FIBONACCI(f):
    teksti=str(LLOGFIBONACCI(f))
    return teksti.encode()

#funksioni per konvertim, varesisht nga opsioni i zgjedhur nga klienti
def KONVERTIMI(opt,vlera):
    nr = int(vlera)
    if opt=='KilowattToHorsepower':
        a = nr*1.341
        teksti = str(a)+" Horsepower"
        return teksti.encode()
    elif opt=='HorsepowerToKilowatt':
        a= nr/1.341
        teksti = str(a)+" Kilowatt"
        return teksti.encode()
    elif opt=='DegreesToRadians':
        a = nr*math.pi/180
        teksti = str(a)+ " Radians"
        return teksti.encode()
    elif opt=='RadiansToDegrees':
        a = nr*180/math.pi
        teksti = str(a)+" Degrees"
        return teksti.encode()
    elif opt=='GallonsToLiters':
        a = nr*3.785
        teksti = str(a)+ " Liters"
        return teksti.encode()
    elif opt=='LitersToGallons':
        a = nr/3.785
        teksti = str(a)+ " Gallons"
        return teksti.encode()
    else:
        return gabim.encode()

#funksioni qe e kthen nje nga numrat 1-10 ne fjale
def NRTEKST(num):
    y = int(num)
    if y == 1:
        teksti = "Nje"
        return teksti.encode()
    elif y == 2:
        teksti = "Dy"
        return teksti.encode()
    elif y == 3:
        teksti = "Tre"
        return teksti.encode()
    elif y == 4:
        teksti = "Kater"
        return teksti.encode()
    elif y == 5:
        teksti = "Pese"
        return teksti.encode()
    elif y == 6:
        teksti = "Gjashte"
        return teksti.encode()
    elif y == 7:
        teksti = "Shtate"
        return teksti.encode()
    elif y == 8:
        teksti = "Tete"
        return teksti.encode()
    elif y == 9:
        teksti = "Nente"
        return teksti.encode()
    elif y == 10:
        teksti = "Dhjete"
        return teksti.encode()
    else:
        print("Gabim!")
#funksioni qe kthen fuqine e 2 ose rrenjen katrore te nje numri
def MATH(opt,y):
    b = int(y)
    if opt == 'POW2':
         z = pow(b,2)
         teksti = str(z)
         return teksti.encode()
    if opt == 'SQRT':
         z = math.sqrt(b)
         teksti = str(z)
         return teksti.encode()

switch={"IPADRESA":IPADRESA,"FIBONACCI":FIBONACCI,"BASHKETINGELLORE":BASHKETINGELLORE,
          "PRINTIMI":PRINTIMI,"KOHA":KOHA,
          "LOJA":LOJA,"NUMRIIPORTIT":NUMRIIPORTIT,"EMRIIKOMPJUTERIT":EMRIIKOMPJUTERIT,"KONVERTIMI":KONVERTIMI, "NRTEKST":NRTEKST,"MATH":MATH}

def next(message,address):
 
  try:
    while True:
        teksti = message
        a=teksti.decode().split(' ')
        if a[0] not in switch:
            serverSocket.sendto(gabim.encode(),address)
            break
        else:       
            if len(a)==1:
                l=find(a[0])
                print(l.decode())
                serverSocket.sendto(l,address)
                break
            elif len(a)==2:
                l=findtwo(a[0],a[1])
                print(l.decode())
                serverSocket.sendto(l,address)
                break
            elif len(a)==3:
                        l=findthree(a[0],a[1],a[2])
                        print(l.decode())
                        serverSocket.sendto(l,address)
                        break
            else:
                serverSocket.sendto(gabim.encode(),address)
                break
  except:
          serverSocket.sendto(gabim.encode(),address)
          


while True:
    try:
        message, address = serverSocket.recvfrom(128)
        print("\nKlienti " +gethostname()+" u lidh ne serverin %s me port %s "% address+"\n")
        start_new_thread(next,(message,address,))
    except:
        pass