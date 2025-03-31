from absclass import Administrador_Notificaciones
from absclass import NotificadorCE as NCE, NotificadorSMS as NSMS, NotificadorSlack as NSLACK
import os

a=1
while(a==1):
    print("Elije por donde vas a enviar el mensaje")
    print("1. Email")
    print("2. SMS")
    print("3. Slack")
    opcion = input("Opcion: ")
    try:
        opcion = int(opcion)
    except ValueError:
        print("Opcion no valida")
        continue

    if opcion == 1:
        na = NCE
        break
    elif opcion == 2:
        na = NSMS
        break
    elif opcion == 3:
        na = NSLACK
        break

if opcion==1 | opcion==2:
    n1 = Administrador_Notificaciones()
    n1.enviar(input("Escribe al destinatario: "),input("Escribe el mensaje a enviar: "), na)
else:
    n1 = Administrador_Notificaciones()
    n1.enviar("slack",input("Escribe el mensaje a enviar: "), na)
