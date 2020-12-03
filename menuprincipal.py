mode_joc=0 #Mode de Joc. [1=Jugador VS Jugador/2=Jugador VS Màquines]
mode_ok=False
while mode_ok==False:
    print("***MENÚ PRINCIPAL:***\n" #Menú principal
          "***ELEGEIX UN MODE DE JOC***\n"
          "1. Jugador VS Jugador\n"
          "2. Jugador VS Màquina")
    mode_joc=input("Elecció: ")
    if mode_joc=="1" or mode_joc=="2": #Elecció correcte del mode de joc.
        mode_joc=int(mode_joc)
        mode_ok=True
    else:
        print("Opció incorrecte!") #Validació d'entrada correcta.
        mode_ok=False
print(mode_joc)