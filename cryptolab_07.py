# cryptolab_07.py - Cifrado asimetrico (RSA)
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

if __name__ == "__main__":
    print("=== CRYPTOLAB 07: CIFRADO ASIMETRICO (RSA) ===")
    llave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    llave_publica = llave_privada.public_key()
    print("Par de llaves RSA (2048 bits) generado con exito.\n")

    mensaje = input("Escribe un mensaje secreto: ").encode('utf-8')
    mensaje_cifrado = llave_publica.encrypt(
        mensaje,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"\nMensaje cifrado (hex):\n{mensaje_cifrado.hex()[:60]}...\n")

    mensaje_descifrado = llave_privada.decrypt(
        mensaje_cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Mensaje descifrado con llave privada:\n{mensaje_descifrado.decode('utf-8')}")
