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

  
# Ejecutar el juego
jugar_bingo()
