#Juego te-te-ti por consola

#Agradesco a mis padres por acompañarme siempre y al forito #21 por
#haberme ayudado en el aprendizaje de este lenguaje de programacion

#v 5.0
#Se agrego una nueva función (inicio) que facilita y simplifica el codigo
#Se agrego la opción de poder seguir jugando una vez terminada la partida



#v 4.0
#Se reescribió el formato de la lista (antes era por cordenadas "x-y" Ahora
#es lineal) y con ello tambien se reescribió toda la mecanica desde la forma
#de representar la pantalla, hasta como buscar TA-TE-TI.
#Se arreglo un bug que impedia ver el titulo del juego en la parte alta
#de la pantalla
#Se añadio titulo a la consola de windows



#v 3.0

#Se arregló el sistema de fin de partida
#Ahora ya se termina el juego si no hay mas espacios vacios
#indicando "Empate"
#Se arregló tambien la forma en la que se ve la grilla en pantalla




#V 2.0

#Se reescribió y mejoró el sistema de entradas con respecto a la
#anterior versión.
#Ahora ya no se cierra solo al introducir una posición incorrecta, en todo
#caso pide que se vuelva a intentar.




import os

#pone el titulo "TATETI" en la consola de windows
os.system('Title ' + 'TATETI')


def pantalla():
    """dibuja la grilla y limpia y actualiza la pantalla"""

    os.system('cls')
    print('   ***TA-TE-TI*** \n\n\n')
    print('       %s | %s | %s' % (lista[6],lista[7],lista[8]))
    print('      -----------')
    print('       %s | %s | %s' % (lista[3],lista[4],lista[5]))
    print('      -----------')
    print('       %s | %s | %s' % (lista[0],lista[1],lista[2]))


def tateti():
    """busca en la grilla si hay tateti
    si no lo encuentra devuelve -1"""
    
    xo = ['x','o']
#buscando tateti en las filas
    if lista[6] == lista[7] == lista[8] and lista[6] in xo:
        return (lista[6])

    elif lista[3] == lista[4] == lista[5] and lista[3] in xo:
        return (lista[3])

    elif lista[0] == lista[1] == lista[2] and lista[0] in xo:
        return (lista[0])


#buscando tateti en las columnas
    elif lista[6] == lista[3] == lista[0] and lista[6] in xo:
        return (lista[6])

    elif lista[7] == lista[4] == lista[1] and lista[7] in xo:
        return(lista[7])

    elif lista[8] == lista[5] == lista[2] and lista[8] in xo:
        return(lista[8])

#buscando tateti en las diagonales
    elif lista[6] == lista[4] == lista[2] and lista[6] in xo:
        return (lista[6])
    
    elif lista[8] == lista[4] == lista[0] and lista[8] in xo:
        return(lista[8])

    else:
        return(-1)

def entrada(n):
    """pide las cordenadas donde poner la "x" o "o"
    usando como referencia la disposoción del teclado numerico
    789
    456
    123

    n sera "x" o "o"
    """
    while True:
        if n == 'x':
            numero = input ('¿Donde poner la "x"? ')
        elif n == 'o':
            numero = input ('¿Donde poner la "o"? ')

        if numero not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('solo puede ser un numero (1~9)!')

        elif numero not in jugadas:
            jugadas.append(numero)
            return (numero)
            break
        else:
            print('posición ocupada!')
    
    
def matriz(n, numero):
    """guarda 'n' en la lista siguiendo la matriz del ta-te-ti"""

    if numero == '1':
        lista[0] = n
    elif numero == '2':
        lista[1]=n
    elif numero == '3':
        lista[2]=n
    elif numero == '4':
        lista[3]=n
    elif numero == '5':
        lista[4]=n
    elif numero == '6':
        lista[5]=n
    elif numero == '7':
        lista[6]=n
    elif numero == '8':
        lista[7]=n
    elif numero == '9':
        lista[8]=n
        
    



def inicio():
    """inicializa todos los datos del juego"""

    global jugadas
    global lista
    jugadas = []    #aqui guardaré las jugadas hechas
    lista = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ',]
    pantalla()

def rejugar():
    """pregunta si vuelve a jugar"""
    while True:
        rejugar = input('\n\n¿Volver a jugar? (1= SI 2=NO) ')
        if rejugar not in ['1', '2']:
            print('solo puede ser "1" (Si) o "2"(No)')
        elif rejugar == '1':
            return(True)
        else:
            return(False)


#inicio

inicio()
print('\n\n jugador x')

while True:
#jugador 1
    matriz('x', entrada('x'))
    pantalla()
    if tateti() != -1:
        print('\n\n El jugador "x" es el ganador')
        if rejugar():
            inicio()
        else:
            break
        
    if ' ' not in lista:
        print('\n\n*** Empate ***')
        if rejugar():
            inicio()
        else:
            break

#jugador 2
    matriz('o',entrada('o'))
    pantalla()
    if tateti() != -1:
        print('\n\n El jugador "o" es el ganador')
        if rejugar():
            inicio()
        else:
            break
        
    if ' ' not in lista:
        print('\n\n*** Empate ***')
        if rejugar():
            inicio()
        else:
            break

print ('\n\n*** FIN ***')
input()
