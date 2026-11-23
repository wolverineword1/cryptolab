# cryptolab_05.py - Salting (Sal criptografica)
import hashlib
import secrets

def registrar_usuario(contrasena):
    sal = secrets.token_hex(16)
    hash_seguro = hashlib.sha256((sal + contrasena).encode('utf-8')).hexdigest()
    return sal, hash_seguro

def verificar_login(contrasena_ingresada, sal_guardada, hash_guardado):
    hash_intento = hashlib.sha256((sal_guardada + contrasena_ingresada).encode('utf-8')).hexdigest()
    return hash_intento == hash_guardado

if __name__ == "__main__":
    print("=== CRYPTOLAB 05: REGISTRO CON SALT ===")
    sal_1, hash_1 = registrar_usuario("dragon123")
    sal_2, hash_2 = registrar_usuario("dragon123")

    print(f"Usuario 1 -> Sal: {sal_1[:10]}... | Hash: {hash_1[:20]}...")
    print(f"Usuario 2 -> Sal: {sal_2[:10]}... | Hash: {hash_2[:20]}...")

    intento = input("\nIngresa tu contrasena para entrar (Usuario 1): ")
    if verificar_login(intento, sal_1, hash_1):
        print("Acceso concedido.")
    else:
        print("Contrasena incorrecta.")
