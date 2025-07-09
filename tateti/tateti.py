from random import randrange #se usará para que la máquina elija posiciones al azar

# Mostrar el tablero
def mostrar_tablero(tablero):
    print("\n")
    for i in range(3): 
        print(" ", tablero[i][0], "|", tablero[i][1], "|", tablero[i][2])#muestra los tres elementos de la fila actual i, separados con barras
        if i < 2: 
            print(" ---|---|---")
    print("\n")

# Verificar si alguien gano
def verificar_ganador(tablero, jugador):#función que revisa si jugador tiene tres fichas en línea
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:#si todos los valores de una fila son iguales al jugador gano
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:#si todos los valores de una columna son iguales al jugador  gano
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:#revisa la diagonal principal 
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:#revisa la diagonal secundaria 
        return True
    return False
    

# Casillas vacías
def casillas_libres(tablero):# función que devuelve una lista de todas las posiciones vacías
    libres = []#creamos una lista vacía para guardar coordenadas libres
    for i in range(3):
                       #recorremos la matriz 3x3, fila por fila y columna por columna
        for j in range(3):
            if tablero[i][j] == " ":
                       #si la casilla está vacía (" "), agregamos su posición (i, j) a la lista
                libres.append((i, j))
    return libres#devuelve la lista de posiciones libres

# Jugada aleatoria de la máquina
def jugada_maquina(tablero, maquina):# esta función juega por la máquina. Recibe el tablero y su ficha ("X" o "O")
    libres = casillas_libres(tablero)#llama a casillas_libres() para ver dónde puede jugar
    if libres: 
        i, j = libres[randrange(len(libres))]#elige una posición al azar con randrange()
        tablero[i][j] = maquina#coloca la ficha de la máquina en esa posición

# Función principal del juego
def jugar():
    while True:
        tablero = [[" " for _ in range(3)] for _ in range(3)]#crea una matriz 3x3 de espacios vacíos
        # Elegir ficha
        while True:
            jugador = input("¿Querés jugar con X o O? ").upper()
            if jugador in ["X", "O"]:
                break
            else:
                print("Opción inválida. Escribí X o O.")

        maquina = "O" if jugador == "X" else "X"#si el jugador eligió "X", la máquina será "O", y viceversa
        turno = "X"  # X siempre empieza
        ganador = None#para guardar quién gana

        for _ in range(9):#repite el juego hasta 9 veces (máximo de movimientos)
            mostrar_tablero(tablero)#Muestra el tablero actual

            if turno == jugador:#verifica si es el turno del jugador
                print("Tu turno:")
                while True:
                    try:#usa try/except para manejar errores de entrada.
                        fila = int(input("Fila (0, 1 o 2): "))#convierte la fila y columna a números
                        col = int(input("Columna (0, 1 o 2): "))
                        if tablero[fila][col] == " ":#si la casilla está libre
                            tablero[fila][col] = jugador#pone la ficha del jugador y sale del bucle
                            break
                        else:
                            print("Esa casilla ya está ocupada.")
                    except (ValueError, IndexError):#si el usuario pone un texto o número inválido, se muestra un mensaje
                        print("Entrada inválida. Ingresá números entre 0 y 2.")
            else:
                print("Turno de la máquina...")
                jugada_maquina(tablero, maquina)#llama a jugada_maquina() para que elija una casilla al azar

            if verificar_ganador(tablero, turno):#después de cada jugada, revisa si el jugador actual ganó
                ganador = turno#si ganó, guarda al ganador y sale del bucle for
                break

            turno = maquina if turno == jugador else jugador#si ganó, guarda al ganador y sale del bucle for(y al reves)

        mostrar_tablero(tablero)# muestra cómo terminó el tablero
        if ganador:
            if ganador == jugador:#informa si ganó el jugador, la máquina o si fue empate
                print("¡Ganaste!")
            else:
                print("Suerte para la proxima")
        else:
            print("¡Empate!")

        # preguntar si quiere volver a jugar
        otra = input("¿Querés jugar otra vez? (s/n): ").lower()
        if otra != "s":
            print("¡Gracias por jugar!")
            break

# Iniciar el juego
jugar()