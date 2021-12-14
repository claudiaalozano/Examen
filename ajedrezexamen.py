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