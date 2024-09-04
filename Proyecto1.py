import random
#Este es una modif desde Github
def generar_numeros_usuario():
    # Genera 5 números aleatorios entre 1 y 20 para el usuario
    return random.sample(range(1, 21), 5)

def generar_numeros_bingo():
    # Genera 5 números aleatorios entre 1 y 20 para el bingo
    return random.sample(range(1, 21), 5)

def jugar_bingo():
    # Generar los números para el usuario
    numeros_usuario = generar_numeros_usuario()
    print(f"Tu cartón de Bingo: {numeros_usuario}")

    # Generar los números para el bingo
    numeros_bingo = generar_numeros_bingo()
    print(f"Números del Bingo: {numeros_bingo}")

    # Comprobar coincidencias
    coincidencias = set(numeros_usuario).intersection(numeros_bingo)
    print(f"Números acertados: {list(coincidencias)}")

    # Cantidad de aciertos
    aciertos_usuario = len(coincidencias)
    print(f"Tienes {aciertos_usuario} acierto(s).")

    # Mensajes según el número de aciertos
    if aciertos_usuario == 5:
        print("¡Felicidades! Has ganado un millón de dólares.")
    elif aciertos_usuario == 4:
        print("¡Felicidades! Has ganado 500 mil dólares.")
    elif aciertos_usuario == 3:
        print("¡Felicidades! Has ganado otro cartón.")
    elif aciertos_usuario >= 2:
        print("¡Sigue intentando!")
    else:
        print("No has acertado suficientes números. ¡Inténtalo de nuevo!")

# Ejecutar el juego
jugar_bingo()


