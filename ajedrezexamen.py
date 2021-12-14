from random import randint, randit 

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

