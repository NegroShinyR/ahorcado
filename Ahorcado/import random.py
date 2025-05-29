import random

# Dibujo del ahorcado según errores
ahorcado = [
    """
       +---+
           |
           |
           |
          ===""",
    """
       +---+
       O   |
           |
           |
          ===""",
    """
       +---+
       O   |
       |   |
           |
          ===""",
    """
       +---+
       O   |
      /|   |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
]

# Lista ampliada de 50 palabras aleatorias
palabras = [
    "jirafa", "elefante", "murcielago", "computadora", "serpiente", "pantalla", "raton",
    "teclado", "ventana", "pizarra", "estudiante", "profesor", "cuaderno", "lapicero",
    "escritorio", "reloj", "bicicleta", "celular", "auriculares", "cargador", "television",
    "lavadora", "aspiradora", "refrigerador", "microondas", "bocina", "impresora", "cable",
    "consola", "videojuego", "internet", "robot", "planeta", "astronauta", "galaxia",
    "universo", "estacion", "ciencia", "laboratorio", "experimento", "formula", "molecula",
    "atomo", "energia", "fuerza", "gravedad", "fisica", "quimica", "biologia", "genetica"
]

def jugar():
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 0
    max_intentos = len(ahorcado) - 1
    letras_dichas = []

    while intentos < max_intentos:
        print(ahorcado[intentos])
        print("\nLetras ya dichas:")
        print("".join(sorted(letras_dichas)))
        
        estado_palabra = [letra if letra in letras_adivinadas else "-" for letra in palabra]
        print("\nPalabra:", "".join(estado_palabra))

        if "".join(estado_palabra) == palabra:
            print("\n¡Ganaste! La palabra era:", palabra)
            break

        letra = input("\nIngresa una letra: ").lower()
        
        if not letra.isalpha() or len(letra) != 1:
            print(" Ingresa solo una letra valida.")
            continue
        if letra in letras_dichas:
            print(" Ya dijiste esa letra.")
            continue

        letras_dichas.append(letra)

        if letra in palabra:
            letras_adivinadas.append(letra)
        else:
            intentos += 1

    else:
        print(ahorcado[intentos])
        print("\nPerdiste... ")
        print("La palabra era:", palabra)

def main():
    while True:
        jugar()
        jugar_otra = input("\n¿Jugar de nuevo? (s/n): ").lower()
        if jugar_otra != "s":
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
