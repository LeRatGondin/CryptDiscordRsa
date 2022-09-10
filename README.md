# Chiffrement Rsa Discord

## Description
Un selfbot permettant une discuttion entre deux personnes de maniere securisée en utilisant le chiffrement [RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA)

## Installation
Il faut juste installer [python](https://www.python.org/downloads/) et installer les dependances du programme 
Attention la dependance discord.py-self va n'est pas compatible avec discord.py donc veuillez le desinstaller avant d'installer les dependances

Il vous faudra également mettre votre [token discord](https://mediaboss.fr/trouver-token-discord/) et le mettre ici 
![image](https://user-images.githubusercontent.com/44407018/187325126-b6afc9bc-e6ea-4044-b13d-18dddd7909f7.png)


##  Utilisation
Les deux personnes devront créer des clés rsa grâce a la commande -createkey (demande un mdp dans le terminal)

Ensuite elles devrons d'echanger leurs clés publiques avec la commande -exportkey pour envoyer la commande que l'autre personne devra executer

Et pour lancer la discussion chiffrée vous devrez tout les deux lancer la commande -rsastart avec un ping de l'autre utilisateur (demande un mdp dans le terminal)

Et vous pourrez discutter de maniere securisée sur discord sans que rien ne soit enregistré 

## Images 
Commande -exportkey

![image](https://user-images.githubusercontent.com/44407018/187326228-29ec16b1-9e30-42b5-9cce-25e3778d2c6e.png)

Commande -rsastart

![image](https://user-images.githubusercontent.com/44407018/187326526-586a9d2e-d80d-4c8c-a38d-a35bd1aa525a.png)

