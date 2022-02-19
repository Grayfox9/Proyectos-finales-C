#Las preguntas que te irá haciendo la esfinge corresponden a los print de esta plantilla
#Por favor completa cada reto

#Clase 1 Proyecto: Definidendo la aventura

#Reto 1 - Pon tu respuesta después del print
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

botas = 20
cuerda = 15.5
gafas = 12.5
agua = 3.25
cantinflora = 5.5
linterna = 20.5
snacks = 8.2
minimedkit = 30
mapa = 10
gps =35
reloj = 16.3
batería = 5
camara = 28.6
brujula = 16


#Reto 2 - Pon tu respuesta después de cada print
print("Lista tres objetos del equipamiento: Nombre y valor")

print( "reloj", reloj)

print( "cantinflora", cantinflora)

print( "mapa", mapa)


print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

camara_batería = camara + batería

mapa_gps_brujula = mapa + gps + brujula

cantinflora_agua = cantinflora + agua

linterna_batería = linterna + batería

print("Camara con batería", camara_batería)

print("Pack: mapa, brujula, gps", mapa_gps_brujula)

print("Cantinflora con agua", cantinflora_agua)

print("Linterna con batería", linterna_batería)


print("¿El precio del agua en botella es menor al de la linterna funcional?")


print( cantinflora_agua < linterna_batería)



print("¿Cuanto valdría comprar unos snacks y una brujula?")

print(snacks + brujula)




print("¿Si tienes 100 puntos, te alcanza para comprar unas botas?")

print( botas <= 100)




#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("La esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")

backpack = 0

if camara_batería + linterna_batería + cantinflora_agua + snacks + reloj <= 200:
    backpack = camara_batería + linterna_batería + cantinflora_agua + snacks + reloj
    print("El valor total de los items en tu mochila es menor a 200. Valor actual: ", backpack)

elif camara_batería + linterna_batería + cantinflora_agua + snacks <= 200:
    backpack = camara_batería + linterna_batería + cantinflora_agua + snacks
    print("El valor de total de los items en tu mochila es mayor a 200. Valor actual: ", backpack)

else:
    print("Tu mochila sobrepasa los 200 trekjuls")



#Reto 4 - Pon tu respuesta después del print
print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")

backpack2 = 0
while(backpack2 <= 200):
    backpack2 += cantinflora_agua
    print("Segunda mochila: ", backpack2)

backpack2 -= cantinflora_agua
print("Hay sobrecarga de cantinfloras con agua. El valor limite actual de la segunda mochila es: ", backpack2)




#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")

bp1_actualizada = {
    "cantinflora_agua" : {"Cantidad": 1, "valor_unitario": cantinflora_agua},
    "camara_batería" : {"Cantidad": 1, "valor_unitario": camara_batería},
    "linterna_batería" : {"Cantidad": 1, "valor_unitario": linterna_batería},
    "snacks" : {"Cantidad": 1, "valor_unitario": snacks},
    "reloj" : {"Cantidad": 1, "valor_unitario": reloj}
}

bp2_actualizada = {
    "cantinflora_agua" : {"cantidad": 2, "valor_unitario": cantinflora_agua}
}





#Reto 5 - Pon tu respuesta después del print
print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")

vehiculo = [{}] * 8

for compartimiento in range(8):
    vehiculo[compartimiento] = {
        "cantinflora_agua" : {"Cantidad": 1, "valor_unitario": cantinflora_agua},
        "camara_batería" : {"Cantidad": 1, "valor_unitario": camara_batería},
        "linterna_batería" : {"Cantidad": 1, "valor_unitario": linterna_batería},
        "snacks" : {"Cantidad": 1, "valor_unitario": snacks},
        "reloj" : {"Cantidad": 1, "valor_unitario": reloj}
    }
    print("Has armado una mochila para el compartimiento: ", compartimiento + 1)

for backpack in vehiculo:
    print(backpack)

#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")



def agregarElementosAMochilas():
    for compartimiento in range(3):
        vehiculo[compartimiento] = {
            "cantinflora_agua" : {"Cantidad": 1, "valor_unitario": cantinflora_agua},
            "linterna_batería" : {"Cantidad": 2, "valor_unitario": linterna_batería},
            "snacks" : {"Cantidad": 4, "valor_unitario": snacks},
            "brujula" : {"Cantidad": 2, "valor_unitario": brujula},
        }
    imprimir(vehiculo)
    calcularTotalElementosEnMochilas(vehiculo)

def calcularTotalElementosEnMochilas(vehiculo):
    total_elementos_mochilas = {}

    print("Calculo de Items en Backpacks")
    for backpack in vehiculo:
        for elemento, detalle in backpack.items():
            if elemento in total_elementos_mochilas:
                total_elementos_mochilas[elemento] += detalle["Cantidad"]
            else:
                total_elementos_mochilas[elemento] = detalle["Cantidad"]

    print(total_elementos_mochilas)

def imprimir(estructura):
    for objeto in estructura:
        print(objeto)

agregarElementosAMochilas()
