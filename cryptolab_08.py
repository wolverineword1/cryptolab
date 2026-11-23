# cryptolab_08.py - Firmas digitales (RSA)
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

if __name__ == "__main__":
    print("=== CRYPTOLAB 08: FIRMAS DIGITALES (RSA) ===")
    llave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    llave_publica = llave_privada.public_key()

    documento = input("Escribe el contrato o mensaje a firmar: ").encode('utf-8')
    firma = llave_privada.sign(
        documento,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(f"\nFirma digital generada:\n{firma.hex()[:60]}...\n")

    print("--- Verificando autenticidad ---")
    try:
        llave_publica.verify(
            firma,
            documento,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("FIRMA VALIDA: El documento es autentico y no fue alterado.")
    except InvalidSignature:
        print("ALERTA: Firma invalida o documento modificado.")

    documento_alterado = documento + b"!"
    try:
        llave_publica.verify(
            firma,
            documento_alterado,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("FIRMA VALIDA.")
    except InvalidSignature:
        print("PRUEBA DE SABOTAJE: Se detecto que el mensaje fue alterado (+ '!') y se rechazo la firma.")
