


def Deter_classIP():
    adresse_IP = input("Entrez une adresse IP : ")

    #  separation de l'IP par des points
    parties_IP = adresse_IP.split('.')

    #  classe A (1.0.0.0 à 126.255.255.255)
    if int(parties_IP[0]) >= 1 and int(parties_IP[0]) <= 126:
        print("L'adresse IP", adresse_IP, "appartient à la classe A.")
    
    # classe B (128.0.0.0 à 191.255.255.255)
    elif int(parties_IP[0]) >= 128 and int(parties_IP[0]) <= 191:
        print("L'adresse IP", adresse_IP, "appartient à la classe B.")
    
    # classe C (192.0.0.0 à 223.255.255.255)
    elif int(parties_IP[0]) >= 192 and int(parties_IP[0]) <= 223:
        print("L'adresse IP", adresse_IP, "appartient à la classe C.")
        # 224.0.0.0/8- 239.255.255.255
    elif int(parties_IP[0]) >= 224 and int(parties_IP[0]) <= 239:
        print("L'adresse IP", adresse_IP, "est une adresse de multi-diffusion.")

      # 240.0.0.0/8-  255.255.255.254
    elif int(parties_IP[0]) >= 240 and int(parties_IP[0]) <= 225:
        print("L'adresse IP", adresse_IP, "est une Classe Experimental, qui n'ai pas utilisable encore.")
    
      # 
      # 2255.255.255.255	
    elif int(parties_IP[0]) >= 255 and int(parties_IP[0]) <= 225:
        print("L'adresse IP", adresse_IP, "est une adresse de diffusions limité à un LAN.")

        # 127.0.0.0/8-     127.255.255.255
    elif int(parties_IP[0]) >= 127 and int(parties_IP[0]) <= 127:
        print("L'adresse IP", adresse_IP, "est une adresse de Bouclage.")

    # Si l'adresse IP ne correspond à aucune classe A, B ou C
    else:
        print("L'adresse IP", adresse_IP, "Addresse inconnu")

# J'appel m'a fonction 
Deter_classIP()

"""

import ipaddress

def check_ipv6(ipv6_address):
    try:
        ipaddress.IPv6Address(ipv6_address)
        print("L'adresse IPv6", ipv6_address, "est valide.")
    except ipaddress.AddressValueError:
        print("L'adresse IPv6", ipv6_address, "est invalide.")

# Exemple d'utilisation
ipv6_address = input("Entrez une adresse IPv6 : ")
check_ipv6(ipv6_address)

"""