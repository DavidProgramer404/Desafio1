import sys  # Importa el módulo sys.
import random  # Importa el módulo random.

# Crea una lista de opciones válidas para el juego.
opciones_validas = ['piedra', 'papel', 'tijera']

# Verifica si se proporcionó exactamente un argumento en la línea de comandos y si ese argumento es una opción válida.
if len(sys.argv) != 2 or sys.argv[1].lower() not in opciones_validas:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    print("Opciones válidas:", ", ".join(opciones_validas))
else:
    # Si se proporciona un argumento válido, asigna el valor del argumento proporcionado por el usuario.
    usuario = sys.argv[1].lower()
    opciones = ['piedra', 'papel', 'tijera']
    
    # La computadora elige aleatoriamente una opción de la lista de opciones.
    computadora = random.choice(opciones)
    
    # Imprime la elección del usuario y la elección de la computadora.
    print(f'Tu jugaste {usuario.capitalize()}')
    print(f'Computadora jugó {computadora.capitalize()}')

    # Evalúa quién gana o si hay un empate, y muestra el resultado.
    if usuario == computadora:
        print("Empate")
    elif (usuario == 'piedra' and computadora == 'tijera') or \
        (usuario == 'papel' and computadora == 'piedra') or \
        (usuario == 'tijera' and computadora == 'papel'):
        print("Ganaste!!")
    else:
        print("Perdiste")

        #COMANDO TERMINAL -> python cachipun.py "selecciona -> piedra papel o tijera"
