# Examen

mi dirección de github es: https://github.com/claudiaalozano/Examen.git

CÓDIGO AJEDREZ:
```from random import randint


tableroajedrez =  [
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
    [' ', ' ', ' '], 
    ]

x = randint(0,2)
y = randint(0,2)
z = randint(0,2)
a = randint(0,2)
b = randint(0,2)
c = randint(0,2)

while x == a:
    a = randint(0,2)
while y == b:
    b = randint(0,2)
while z == c:
    c = randint(0,2)

#posicion piezas
#(tableroajedrez[x])[0] = "TORREBLANCA1"
#(tableroajedrez[y])[1] = "TORREBLANCA2"
#(tableroajedrez[z])[2] = "TORREBLANCA3"
#(tableroajedrez[a])[0] = "TORRENEGRA1"
#(tableroajedrez[b])[1] = "TORRENEGRA2"
#(tableroajedrez[c])[2] = "TORRENEGRA3"

(tableroajedrez[x])[0] = chr(0x2656)
(tableroajedrez[y])[1] = chr(0x2656)
(tableroajedrez[z])[2] = chr(0x2656)
(tableroajedrez[a])[0] = chr(0x265C)
(tableroajedrez[b])[1] = chr(0x265C)
(tableroajedrez[c])[2] = chr(0x265C)



def movimientopiezablanca(tableroajedrez,a,b,c,x,y,z):
    print(tableroajedrez)   
    try:
        if (tableroajedrez[a+1])[0] != " " and (tableroajedrez[a-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif (tableroajedrez[a+1])[0] == " " and (tableroajedrez[a-1])[0] == " ":
            try:
                if (tableroajedrez[x+1])[0] == " " :  (tableroajedrez[x+1])[0] = (tableroajedrez[x])[0] = (tableroajedrez[x])[0]  
            except:
                pass
            print(tableroajedrez)
    except:
        pass
    

    try:
        if (tableroajedrez[x+1])[0] != " " and (tableroajedrez[x-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif (tableroajedrez[x+1])[0] == " " and (tableroajedrez[x-1])[0] == " ":
            try:
                if (tableroajedrez[a+1])[0] == " " :  (tableroajedrez[a+1])[0] = (tableroajedrez[a])[0] = (tableroajedrez[a])[0]  
            except:
                pass
            print(tableroajedrez)
    except:
        pass
    
    try:
        if (tableroajedrez[b+1])[0] != " " and (tableroajedrez[b-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif (tableroajedrez[b+1])[0] == " " and (tableroajedrez[b-1])[0] == " ":
            try:
                if (tableroajedrez[y+1])[0] == " " :  (tableroajedrez[y+1])[0] = (tableroajedrez[y])[0] = (tableroajedrez[y])[0]  
            except:
                pass
            print(tableroajedrez)
    except:
        pass

    try:
        if (tableroajedrez[y+1])[0] != " " and (tableroajedrez[y-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif (tableroajedrez[y+1])[0] == " " and (tableroajedrez[y-1])[0] == " ":
            try:
                if (tableroajedrez[b+1])[0] == " " :  (tableroajedrez[b+1])[0] = (tableroajedrez[b])[0] = (tableroajedrez[b])[0]  
            except:
                pass
            print(tableroajedrez)
    except:
        pass

    try:
        if (tableroajedrez[c+1])[0] != " " and (tableroajedrez[c-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif (tableroajedrez[c+1])[0] == " " and (tableroajedrez[c-1])[0] == " ":
            try:
                if (tableroajedrez[z+1])[0] == " " :  (tableroajedrez[z+1])[0] = (tableroajedrez[z])[0] = (tableroajedrez[z])[0]  
            except:
                pass
            print(tableroajedrez)
    except:
        pass

    try:
        if (tableroajedrez[z+1])[0] != " " and (tableroajedrez[z-1])[0] != " ":
            print(tableroajedrez)
            pass
        elif (tableroajedrez[z+1])[0] == " " and (tableroajedrez[z-1])[0] == " ":
            try:
                if (tableroajedrez[c+1])[0] == " " :  (tableroajedrez[c+1])[0] = (tableroajedrez[c])[0] = (tableroajedrez[c])[0]  
            except:
                pass
            print(tableroajedrez)
    except:
        pass

movimientopiezablanca(tableroajedrez,a,b,c,x,y,z)

#printear el tablero

def printeartablero(tableroajedrez):
    contador_indice = 0
    for tableroajedrez[contador_indice] in tableroajedrez:
        print(tableroajedrez[contador_indice])
        contador_indice += 1

printeartablero(tableroajedrez)```

CÓDIGO MINIÓN:
```def minion(s):
    vowels = "AEIOU"
    scoreStuart = 0
    scoreKevin = 0
    s=s.upper()

    for i in range(len(s)):
        if s[i] not in vowels:
            scoreStuart = scoreStuart + (len(s)-i)
        else: 
            scoreKevin = scoreKevin + (len(s)-i)
    
    if scoreStuart>scoreKevin:
        print("Stuart ganador <3, tu puntuación es:" , scoreStuart)
    elif scoreStuart<scoreKevin:
        print("Kevin ganador <3 <3, tu puntuacion es:" , scoreKevin)
    else:
        print("Empatados :( , volved a jugar.")

if __name__ == "__main__":
    s = input("Minion elige la palabra para el juego: ")  
    minion(s)      ```
    
