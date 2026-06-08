Documentation : Connexion SSH

1. Prérequis
Assure-toi d'avoir un accès réseau vers la machine cible et un client SSH installé
(disponible nativement sur Linux/macOS, via PowerShell ou PuTTY sur Windows).

2. Commande de base

ssh utilisateur@adresse_ip_ou_domaine

Remplace utilisateur par ton nom d'utilisateur distant et
adresse_ip_ou_domaine par l'adresse de destination.

3. Authentification par clé (Recommandé)
Pour éviter le mot de passe et renforcer la sécurité :
Générer la paire de clés : ssh-keygen -t ed25519
Copier la clé publique sur le serveur : ssh-copy-id
utilisateur@adresse_ip

4. Options utiles
Port spécifique : ssh -p 2222 utilisateur@adresse
Mode verbeux (debug) : ssh -v utilisateur@adresse