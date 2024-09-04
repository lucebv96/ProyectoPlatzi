import random

def generar_numeros_usuario():
    # Genera 5 números aleatorios entre 1 y 75 para el usuario
    return random.sample(range(1, 76), 5)

def generar_numeros_bingo():
    # Genera 5 números aleatorios entre 1 y 75 para el bingo
    return random.sample(range(1, 76), 5)

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

    # Pedir al usuario que ingrese la cantidad de aciertos
    aciertos_usuario = len(coincidencias)
    print(f"Tienes {aciertos_usuario} acierto(s).")

    # Verificar si hay más de 3 aciertos
    if aciertos_usuario > 3:
        print("¡Felicidades! Has acertado más de 3 números.")
    else:
        print("¡Sigue intentando!")


   
# Ejecutar el juego
jugar_bingo()

