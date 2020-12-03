min_jug=2
max_jug=8
jugadors=[]
abecedari=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "à", "á", "è", "é", "í", "ò", "ó", "ú", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "À", "Á", "È", "É", "Í", "Ò", "Ó", "Ú"]
mode_joc=1 #Mode de Joc. [1=Jugador VS Jugador/2=Jugador VS Màquines]
if mode_joc==1:
    num_jug = 0
    jugadors_ok=False
    while jugadors_ok==False: #Introducció dels jugadors a la llista.
        maxjug_ok=False
        while maxjug_ok==False:
            maxjug=int(input(f"Número de jugadors [Mín {min_jug}, Màx {max_jug}]: "))
            if maxjug>=min_jug and maxjug<=max_jug: #Sustituye el número máximo de jugadores al seleccionado por los usuarios dentro del intérvalo establecido en el archivo de configuración.
                maxjug=max_jug
                maxjug_ok=True
            else:
                print("Número de jugadors no vàlid.")
        noujug=input(f"Entra el nom del Jugador {num_jug+1}: ")
        valid=False
        if noujug.isalnum(): #Comprobació usuari alfanumèric
            valid=True
        if valid==True and noujug[0] in abecedari: #Comprobació inicial lletra
            valid=True
        else:
            valid=False
        if valid==False:
            print("El nom que has introduit no és vàlid. Introdueix un usuari amb caràcters alfanumèrics i que comenci amb una lletra.")
        elif valid==True: #Si el nom està validat, s'afegeix a la llista d'usuaris.
            jugadors.append(noujug)
            print(f"Has afegit amb èxit l'usuari {noujug}.")
            num_jug+=1
            if num_jug>=min_jug and num_jug!=max_jug: #Si ja s'ha assolit el número mínim de jugadors...
                mes_jugs=input("Vols introduir un altre usuari? [S=Sí] [Altre tecla=No]") #Afegir un altre usuari.
                if (mes_jugs=="S" or mes_jugs=="s") and num_jug<max_jug:
                    jugadors_ok=False
                else:
                    jugadors_ok=True
            elif num_jug==max_jug:
                jugadors_ok=True