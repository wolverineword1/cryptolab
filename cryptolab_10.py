import base64
import hashlib
import json
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

ARCHIVO_BOVEDA = Path(__file__).parent / "boveda.dat"

def generar_llave_desde_maestra(contrasena_maestra):
    digest = hashlib.sha256(contrasena_maestra.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)

def cargar_boveda(cipher):
    if not ARCHIVO_BOVEDA.exists():
        return {}
    datos_cifrados = ARCHIVO_BOVEDA.read_bytes()
    datos_json = cipher.decrypt(datos_cifrados).decode("utf-8")
    return json.loads(datos_json)

def guardar_boveda(cipher, datos):
    datos_json = json.dumps(datos).encode("utf-8")
    ARCHIVO_BOVEDA.write_bytes(cipher.encrypt(datos_json))

print("=== CRYPTOLAB 10: BOVEDA DE CONTRASENAS ===")
maestra = input("Ingresa tu contrasena maestra: ")
cipher = Fernet(generar_llave_desde_maestra(maestra))

try:
    boveda = cargar_boveda(cipher)
    print("Boveda desbloqueada con exito.")
except InvalidToken:
    print("ERROR: Contrasena maestra incorrecta. Acceso denegado.")
    exit()

while True:
    print("\n1. Guardar nueva cuenta | 2. Ver cuentas guardadas | 3. Salir")
    opcion = input("Elige una opcion: ").strip()

    if opcion == "1":
        servicio = input("Servicio (ej. Gmail, Netflix): ").strip()
        clave = input("Contrasena del servicio: ").strip()
        boveda[servicio] = clave
        guardar_boveda(cipher, boveda)
        print(f"Cuenta '{servicio}' cifrada y guardada.")
    elif opcion == "2":
        if not boveda:
            print("La boveda esta vacia.")
        for srv, pwd in boveda.items():
            print(f"- {srv}: {pwd}")
    elif opcion == "3":
        print("Boveda cerrada de forma segura.")
        break
