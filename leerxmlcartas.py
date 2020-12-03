from xml.dom import minidom
mazo=[] #Lectura del archivo XML y creación de la lista de tuplas "Mazo"
doc = minidom.parse("Cartas.xml") #Recorregut del fitxer Cartas.xml
cartes = doc.getElementsByTagName("carta") #Afegir cada carta a la llista cartas
for carta in cartes: #Recorrer totes les cartes i anar extreient valors
    valor_real=carta.getElementsByTagName("valor")[0]
    palo=carta.getElementsByTagName("palo")[0]
    valor_juego=carta.getElementsByTagName("valor_juego")[0]
    activa=carta.getElementsByTagName("activa")[0]
    if palo.firstChild.data=="Oros": #Passar el pal de la carta a número de prioritat
        prioridad=1
    elif palo=="Copas":
        prioridad=2
    elif palo=="Espadas":
        prioridad=3
    elif palo=="Bastos":
        prioridad=4
    if activa.firstChild.data=="SI": #Si està activa, crear una tupla amb els valors que volem. Després, afegir la tupla completa a la llista mazo.
        tupla=(int(valor_real.firstChild.data), prioridad, float(valor_juego.firstChild.data))
        mazo.append(tupla)
print(mazo)
