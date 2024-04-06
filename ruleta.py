import random
import string

from palabras import palabras

def obtener_palabra_válida (lista_palabras):
    # Seleccionar una palabra al azar de la lista
    # de palabras válidas.
    palabra = random.choice (palabras)
    
    return palabra.upper()


def ruleta():
    print("== ===")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("= =")
    palabra = obtener_palabra_válida(palabras)


    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas")

        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas
        else '-' for letra in palabra]

        # Mostrar estado del ahorcado
        #print (vidas_diccionario_visual[vidas])

        # Mostrar las letras separadas por un espacio.
        print (f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        # Si la letra escogida por el usuario está en el
        # abecedario y no está en el conjunto de letras
        # que ya se han ingresado, se añade la letra al conjunto
        # de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si la letra está en la palabra, quitar letra
            # de pendientes y si no quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"Tu letra, {letra_usuario} no está en la palabra.")
        # Si la letra escogida ya estaba ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    # jugador llega a 0 vidas
    if vidas == 0:
        print ("AHORCADO! SE ACABÓ")
    else:
        print ("GANASTE")

ruleta()