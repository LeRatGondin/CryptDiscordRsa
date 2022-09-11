# Chiffrement Rsa Discord

## Description
Un selfbot permettant une discuttion entre deux personnes de maniere securisée en utilisant le chiffrement [RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA)

## Installation
Il faut juste installer [python](https://www.python.org/downloads/) et installer les dependances du programme 
Attention la dependance discord.py-self va n'est pas compatible avec discord.py donc veuillez le desinstaller avant d'installer les dependances

Il vous faudra également mettre votre [token discord](https://mediaboss.fr/trouver-token-discord/) et le mettre ici 
![image](https://user-images.githubusercontent.com/44407018/189534410-4291d42f-fb13-4bfc-9fde-2bebe9b53cd7.png)


##  Utilisation
Les deux personnes devront créer des clés rsa grâce a la commande -createkey (demande un mdp dans le terminal)

Ensuite elles devrons d'echanger leurs clés publiques avec la commande -exportkey pour envoyer la commande que l'autre personne devra executer

Et pour lancer la discussion chiffrée vous devrez tout les deux lancer la commande -rsastart avec un ping de l'autre utilisateur (demande un mdp dans le terminal)

Et vous pourrez discutter de maniere securisée sur discord sans que rien ne soit enregistré 

## Sécurité Du Chiffrement
Comme dit plus haut le chiffrement utilise le [RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA) un chiffrement asymetrique avec des clés de 4096 octets

La clé privée n'est pas enregistrée en clair dans les fichiers , elle est chiffrée en [AES](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard) en utilisant le mode d'operation par enchaînement des blocs ou [CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) et il génere le mot de passe aes de 32 octets avec le protocole [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) et un salt de 16 octets généré aléatoirement 

Aucuns message n'est enregisté car supprimé 1 seconde après avoir été envoyé 

## Images 
Commande -exportkey

![image](https://user-images.githubusercontent.com/44407018/187326228-29ec16b1-9e30-42b5-9cce-25e3778d2c6e.png)

Commande -rsastart

![image](https://user-images.githubusercontent.com/44407018/187326526-586a9d2e-d80d-4c8c-a38d-a35bd1aa525a.png)

