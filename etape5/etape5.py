import os, random, sys
print("Au cœur des galaxies de l'Univers",end='\n\n')
print("L‘erreur est humaine, sinon il n‘y aurait pas de gommes à effacer au bout des crayons.")
print("La meilleure façon de l'eviter, est de l'envoyer au cœur des galaxies de l'Univers", end='\n\n\n')

def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

alp = 'f1235ddzddsbsdsdsdpddxxsq0xdvsdsydssaoqid'
val1, val = True, True

for _ in range(33):
    for i in range(1550):
        if i == 425 and val:
            print(f"dsdasddzdps3dsfdxs", end='',file=sys.stdout)
            val = False
        print(alp[random.randint(0,len(alp)-1)],end='',file=sys.stderr)
    print('dvsdqddsssdiddbdqsqodvidxa1dds1sdds25yxddaq3svzxossdysdddasxs2ddxbz5sssdsdddds55idd2apddaoxdsqdpsxxsdaxabs5dosdxs5dbsydsdasddzdps3dsfdxs',file=sys.stdout)
print('\nprenom: ',end='',file=sys.stdout)
for _ in range(1100):
    print(alp[random.randint(0,len(alp)-1)],end='',file=sys.stderr)
prenom = input()
print('\ncle: ',end='',file=sys.stdout)
cle = input()
if cle != 'dsdasddzdps3dsfdxs':
    print('Ooo, Pas le bon client!')
    sys.exit(1)
print("Votre cle pour l'etape6 est:", encrypt('ETAPEE', prenom+'y'))