# cryptolab_01.py - Cifrado Cesar basico
def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    mensaje = "Hola Mundo desde Python"
    clave = 3
    print("Original:", mensaje)
    print("Cifrado:", cifrar_cesar(mensaje, clave))
