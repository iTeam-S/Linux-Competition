import os, sys


def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


prenom = input('prenom utiisé precedement: ')
if decrypt(input("clé de l'etape: "), prenom+'y') != 'ETAPEB':
    print('ERREUR, clé incorrecte...')
    sys.exit(1)

print("Sujet: Ce fameux moyen de Communication")
print("""
Un variables dynamiques utilisées par les différents processus d’un système d’exploitation.
Elles servent à communiquer des informations entre les programmes qui ne se trouvent pas sur la même ligne hiérarchique.
""")
os.system(f"ETAPE3key={encrypt('ETAPEC', prenom+'y')} {os.popen('echo $SHELL').read().strip()}")