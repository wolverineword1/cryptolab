# cryptolab_02.py - Cifrado y descifrado interactivo
def procesar_cesar(texto, desplazamiento, modo):
    if modo == "descifrar":
        desplazamiento = -desplazamiento
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
    print("=== CRYPTOLAB 02 ===")
    accion = input("Quieres cifrar o descifrar?: ").strip().lower()
    mensaje = input("Escribe tu mensaje: ")
    clave = int(input("Ingresa la clave numerica (ej. 3): "))
    print(f"\nResultado ({accion}): {procesar_cesar(mensaje, clave, accion)}")
