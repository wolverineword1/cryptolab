# cryptolab_09.py - Cifrado de archivos reales
from pathlib import Path
from cryptography.fernet import Fernet

if __name__ == "__main__":
    print("=== CRYPTOLAB 09: CIFRADO DE ARCHIVOS REALES ===")
    carpeta = Path(__file__).parent
    archivo_original = carpeta / "secreto.txt"
    archivo_cifrado = carpeta / "secreto.cifrado"
    archivo_recuperado = carpeta / "secreto_recuperado.txt"

    contenido = input("Escribe el contenido secreto para guardar en el archivo: ")
    archivo_original.write_text(contenido, encoding="utf-8")

    llave = Fernet.generate_key()
    cipher = Fernet(llave)

    datos_cifrados = cipher.encrypt(archivo_original.read_bytes())
    archivo_cifrado.write_bytes(datos_cifrados)
    print(f"Archivo cifrado guardado en: {archivo_cifrado.name}")

    datos_descifrados = cipher.decrypt(archivo_cifrado.read_bytes())
    archivo_recuperado.write_bytes(datos_descifrados)
    print(f"Archivo recuperado en: {archivo_recuperado.name}")
    print("Texto recuperado:", archivo_recuperado.read_text(encoding="utf-8"))
