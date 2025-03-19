from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
# Generate the RSA private key
key = rsa.generate_private_key(
public_exponent=65537,
key_size=2048, )

print("\nKey pair is ",key,"\n")

message = b"Balraj Singh"
ciphertext = key.public_key().encrypt(
message,
padding.OAEP(
mgf=padding.MGF1(algorithm=hashes.SHA256()),
algorithm=hashes.SHA256(),
label=None
)
)
print("The cipher text is \n",ciphertext)

plaintext = key.decrypt(
ciphertext,
padding.OAEP(
mgf=padding.MGF1(algorithm=hashes.SHA256()),
algorithm=hashes.SHA256(),
label=None
)
)

print("The plain text is "+ str(plaintext))

plainarr = str(plaintext).split("'")
print("Plainarr: ",plainarr)
print("The message is",plainarr[1])
print("Was that performed correctly? --> ",plaintext == message)
