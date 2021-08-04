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

if len(sys.argv) == 1:
    if os.getuid() != 0:
        print("Non, Il faut lancer en root pour cette fois!")
        sys.exit(1)
    # prenom = input("Entrer votre prenom: ")
    cle = input("Entrer la clé: ")
    # if False:
    #     print(decrypt(input("Entrer la clé: "), prenom+"y") )
    #     print("Désolé, la clé n'est pas du tout correcte, Est-ce vraiment ta clé?")
    #     sys.exit(1)

    os.system('echo dbdfdbdf45d5f4dd45 > readme.txt')
    os.system('chown root:root readme.txt')
    os.system('chmod ugo-rxw readme.txt')
    print("""
    Un fichier readme.txt a été crée, Pour le decrypter et recuperer la clé de la prochaine etape,
    il suffit de relancer le fichier en mettant comme argument le fichier generé.
    """)
else:
    if os.getuid() == 0:
        print("Non, Ce script ne peut pas être lancer en root pour le decryptage")
        sys.exit(1)
    if os.system(f'cat {sys.argv[1]}') != 0:
        print("Stp, Ouvre moi la porte, Je ne peux pas ouvrir ce fichier: PERMISSION DENIED")
        sys.exit(1)
    print("\n==> Waouh, Merci d'avoir ouvert la porte! bien joué\n")

    if os.stat('readme.txt').st_uid == os.getuid():
        print("\n==> Super, ça m'appartient, Merci\n")
        print("Felicitation, vous avez reussi l'etape 2")
        prenom = input("Entrer votre prenom: ")
        print("Votre cle pour l'etape3 est:", encrypt('ETAPEB', prenom+'y'))
        os.system('rm -f readme.txt')
    else:
        print("\nOUPS!! Donne moi la clé stp, ce fichier ne m'appartient pas, Je peux rien faire.")