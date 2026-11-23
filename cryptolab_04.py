# cryptolab_04.py - Ataque de diccionario
import hashlib

def generar_hash(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    contrasena_secreta = "dragon123"
    hash_objetivo = generar_hash(contrasena_secreta)

    print("=== CRYPTOLAB 04: ATAQUE DE DICCIONARIO ===")
    print(f"Hash capturado: {hash_objetivo}\n")

    diccionario = ["123456", "password", "admin", "qwerty", "dragon123", "welcome"]
    encontrada = False

    for palabra in diccionario:
        hash_intento = generar_hash(palabra)
        print(f"Probando '{palabra}' -> {hash_intento[:15]}...")
        if hash_intento == hash_objetivo:
            print(f"\nCONTRASENA DESCUBIERTA: '{palabra}'")
            encontrada = True
            break

    if not encontrada:
        print("\nLa contrasena no esta en el diccionario.")
