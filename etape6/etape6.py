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

if os.getuid():
    print("Must run as SU")
    sys.exit(1)

daemon0 = """
#!/bin/bash
while [ 1 ]; do
    echo $1;
    sleep 30;
done;
"""

with open('/root/partA.key','w') as file:
    file.write(daemon0)

daemon1 = f"""
[Unit]
Description= Les parties d'un démons sont en brute comme la partB: 12
After=network.target

[Service]
User=root
Group=root
Restart=always
RestartSec=5
WorkingDirectory=/tmp
ExecStart=echo Oxff45 > /tmp/partC.key

[Install]
WantedBy=multi-user.target

"""


with open('/etc/systemd/system/etape6.service', 'w') as file:
    file.write(daemon1)


os.system('chmod +x /root/partA.key')
os.system('/root/partA.key 36 >/dev/null &')
os.system('systemctl daemon-reload; systemctl start etape6.service')

print("Les Démons sont dans l'ombre, ils font leurs actes comme-ci de rien n'était\n Mais ils sont là sans faire du bruit.")
print('\n\n')
print('Entrer la clé de combinaison à 6 chiffres, Si necessaire, chassez les démons.')
if input('Clé de combinaison: ') != '361245':
    print('Mauvaise clé')
    sys.exit(1)
prenom = input('Entrer votre prenom: ')
print('votre cle pour l etape suivante est:', encrypt('ETAPEF', prenom))


