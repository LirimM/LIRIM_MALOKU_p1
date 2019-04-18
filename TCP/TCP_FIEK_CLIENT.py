import socket
print("                **************  Klienti FIEK TCP **************\n")
#serverName = 'localhost'
serverName=input("Ju lutem shenoni emrin e serverit: ")
#serverPort = 12000
serverPort=input("Ju lutem shenoni portin: ")
serverPort=int(serverPort)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverName,serverPort))

    print("Metodat:                IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRI")
    print("                        IKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI")
    print("IPADRESA:               Shfaq IP address te klientit ne forme dhjetore. ")
    print("NUMRIIPORTIT:           Shfaq portin e klientit. ")
    print("BASHKETINGELLORE:       Merr nje parameter(tekst) dhe tregon numrin e ")
    print("                        bashketingelloreve ne ate fjale.")
    print("PRINTIMI:               Shfaq fjalinë e shtypur ne tekst. Pa hapesirat ne fillim")
    print("                        dhe ne fund.")
    print("EMRIIKOMPJUTERIT:       Shfaq emrin e kompjuterit.")
    print("KOHA:                   Shfaq kohen aktuale.")
    print("LOJA:                   Kthen 7 numra te rastesishem(random) nga rangu [1,49].")
    print("FIBONACCI:              Permban nje argument dhe kthen vleren fibonacci te tij ")
    print("                        numri")
    print("KONVERTIMI:             Pranon dy parametra, ku i pari eshte njeri nga ")
    print("                        konvertimet: KilowattToHorsepower, HorsepowerToKilowatt,")
    print("                        DegreesToRadians, RadiansToDegrees, GallonsToLiters,")
    print("                        LitersToGallons, ndersa tjetri percakton vleren")
    print("                        , metoda shfaq vleren te konvertuar.")
    print("NRTEKST                 Kthen ne tekst numrin e shtypur nga vargu 1-10")
    print("MATH                    Kthen fuqine e 2 ose rrenjen katrore te nr te dhene")
    print("                        parametri i pare eshte POW2 ose SQRT dhe i dyti nr.\n")
    while 1:
 
        try:
            
             var = input("Jeni lidhur me serverin, mund t'a shkruani kerkesen e deshiruar "+"\nOse shenoni EXIT per t'a mbyllur programin\n "+"Shenoni kerkesen: ")
             if var=="EXIT":
                 s.close()
                 break
             elif len(var)>128:
                 print("Numri i lejueshem i karaktereve eshte tejkaluar")
             elif not var:
                 print("Ju lutem shkruani dicka...")
             else: 
                 s.sendall(str.encode(var))
                 data = s.recv(128)
                 if len(data)>128:
                     print("Kemi pranuar me shume se 128 karaktere!")
                 else:
                     print('Te dhenat e pranuara nga serveri', repr(data.decode())+"\n")           
        except:
             print("Ja ka huq serveri...")
             break
except:
    print("\n")
    print("Serveri nuk eshte ne linje!")
    print("\n")
    input("Shtypni nje tast per te mbyllur programin...")