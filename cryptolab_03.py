# cryptolab_03.py - Hashes SHA-256
import hashlib

def generar_hash(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    print("=== CRYPTOLAB 03: HUELLA DIGITAL SHA-256 ===")
    mensaje_1 = input("Escribe una contrasena o mensaje: ")
    hash_1 = generar_hash(mensaje_1)
    print(f"\nHash generado:\n{hash_1}")

    mensaje_2 = input("\nVuelve a escribirlo (o cambia una letra): ")
    hash_2 = generar_hash(mensaje_2)

    if hash_1 == hash_2:
        print("Coincide: El mensaje es identico.")
    else:
        print("Alterado: Los hashes son diferentes.")
        print(f"Nuevo hash:\n{hash_2}")
