from random import randint 

tableroajedrez= [
    [" " , " " , " "],
    [" " , " " , " "],
    [" " , " " , " "],
    ]

x = randint (0,2)
y = randint (0,2)
z = randint (0,2)
a = randint (0,2)
b = randint (0,2)
c = randint (0,2)

#Las fichas enfrentadas no pueden estar en la misma casilla

while x == a:
    a = randint(0,2)
while y == b : 
    b = randint(0,2)
while z == c:
    c = randint(0,2) 

#Posición de las Torres
# (tableroajedrez[x])[0] = TORRE_NEGRA1
# (tableroajedrez[y])[1] = TORRE_NEGRA2
# (tableroajedrez[z])[2] = TORRE_NEGRA3
# (tableroajedrez[a])[0] = TORRE_BLANCA1
# (tableroajedrez[b])[1] = TORRE_BLANCA2
# (tableroajedrez[c])[2] = TORRE_BLANCA3

(tableroajedrez[x])[0] = chr(0x2656)
(tableroajedrez[y])[1] = chr(0x2656)
(tableroajedrez[z])[2] = chr(0x2656)
(tableroajedrez[a])[0] = chr(0x265C)
(tableroajedrez[b])[1] = chr(0x265C)
(tableroajedrez[c])[2] = chr(0x265C)

def movimientopieza(tableroajedrez,a,b,c,x,y,z):
    print(tableroajedrez)
    #movimiento para primeras torres enfrentadas
    try:
        if (tableroajedrez[a+1])[0] != " " and (tableroajedrez[a-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif(tableroajedrez[a+1])[0] == " " and (tableroajedrez[a-1])[0] == " ":
            try:
                if (tableroajedrez[x+1])[0] == " " : 
                    (tableroajedrez[x+1])[0] = (tableroajedrez[x])[0] 
            except:
                pass
                print(tableroajedrez)
    except: 
        pass

    try:
        if (tableroajedrez[x+1])[0] != " " and (tableroajedrez[x-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif(tableroajedrez[x+1])[0] == " " and (tableroajedrez[x-1])[0] == " ":
            try:
                if (tableroajedrez[a+1])[0] == " " :
                    (tableroajedrez[a+1])[0] = (tableroajedrez[a])[0] 
            except:
                pass
                print(tableroajedrez)
    except: 
        pass

    #movimiento para segundas torres 
    try:
        if (tableroajedrez[y+1])[0] != " " and (tableroajedrez[y-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif(tableroajedrez[y+1])[0] == " " and (tableroajedrez[y-1])[0] == " ":
            try:
                if (tableroajedrez[b+1])[0] == " " :
                    (tableroajedrez[b+1])[0] = (tableroajedrez[b])[0] 
            except:
                pass
                print(tableroajedrez)
    except: 
        pass

    try:
        if (tableroajedrez[b+1])[0] != " " and (tableroajedrez[b-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif(tableroajedrez[b+1])[0] == " " and (tableroajedrez[b-1])[0] == " ":
            try:
                if (tableroajedrez[y+1])[0] == " " :
                    (tableroajedrez[y+1])[0] = (tableroajedrez[y])[0]
            except:
                pass
                print(tableroajedrez)
    except: 
        pass

    #movimiento para terceras torres
    try:
        if (tableroajedrez[z+1])[2] != " " and (tableroajedrez[z-1])[2] != " ":
            print(tableroajedrez)
            pass
        elif(tableroajedrez[z+1])[0] == " " and (tableroajedrez[z-1])[0] == " ":
            try:
                if (tableroajedrez[c+1])[0] == " " :
                    (tableroajedrez[c+1])[0] = (tableroajedrez[c])[0] 
            except:
                pass
                print(tableroajedrez)


    except: 
        pass

    try:
        if (tableroajedrez[c+1])[0] != " " and (tableroajedrez[c-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif(tableroajedrez[c+1])[0] == " " and (tableroajedrez[c-1])[0] == " ":
            try:
                if (tableroajedrez[z+1])[0] == " " :
                    (tableroajedrez[z+1])[0] = (tableroajedrez[z])[0] 
            except:
                pass
                print(tableroajedrez)
    except: 
        pass

movimientopieza(tableroajedrez,a,b,c,x,y,z)

#printeo el tablero
def printablero(tableroajedrez):
    contador= 0
    for tableroajedrez[contador] in tableroajedrez:
        print(tableroajedrez[contador])
        contador = contador + 1

printablero(tableroajedrez)