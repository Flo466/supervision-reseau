import socket

def scan_ports():
    # 1. Demander l'adresse IP ou le nom de serveur
    target = input("Entrez l'adresse IP ou le nom de serveur à scanner : ")
    
    # Liste des ports à tester
    ports = [22, 80, 443, 3306]

    print(f"\nScan en cours sur {target}...")

    for port in ports:
        # Création d'un objet socket (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Timeout court pour ne pas attendre trop longtemps si le port est fermé
        s.settimeout(1)
        
        # 2. Test du port (connect_ex retourne 0 si la connexion réussit)
        result = s.connect_ex((target, port))
        
        # 3. Affichage du résultat
        if result == 0:
            print(f"Port {port} : ouvert")
        else:
            print(f"Port {port} : fermé")
        
        # Fermeture du socket
        s.close()

if __name__ == "__main__":
    scan_ports()