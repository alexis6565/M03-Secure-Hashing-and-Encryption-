#simulate a digital signature (sign/verify)
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Generate a private key for use in the signing process
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Sign a message with the private key
message = b"A message I want to sign"

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Signature:", signature.hex())

# To verify the signature, we need the public key
public_key = private_key.public_key()
# Verify the signature with the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except Exception as e:
    print("Signature is invalid:", e)
# Serialize and print the public key in PEM format
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Public Key:\n", pem.decode('utf-8'))





