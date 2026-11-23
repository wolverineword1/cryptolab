# cryptolab_06.py - Cifrado simetrico real (Fernet / AES)
from cryptography.fernet import Fernet

if __name__ == "__main__":
    print("=== CRYPTOLAB 06: CIFRADO SIMETRICO REAL ===")
    llave = Fernet.generate_key()
    cipher = Fernet(llave)
    print(f"Llave generada:\n{llave.decode()}\n")

    mensaje = input("Escribe un mensaje secreto: ")
    mensaje_cifrado = cipher.encrypt(mensaje.encode('utf-8'))
    print(f"\nMensaje cifrado:\n{mensaje_cifrado.decode()}\n")

    mensaje_descifrado = cipher.decrypt(mensaje_cifrado).decode('utf-8')
    print(f"Mensaje descifrado:\n{mensaje_descifrado}")
