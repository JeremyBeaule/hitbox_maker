# hitbox_maker
un logiciel pour detourer vos png et creer leur hitbox au format json pour pouvoir les exploiter dans un jeu 2d
pour l'uiliser, voici l'arborescence que j'utilise:
![image](https://github.com/bottouch/hitbox_maker/assets/47953708/6e8de000-b7a1-4d54-9485-20c4a2c3e051)
et voici l'interieur des fichiers:
![image](https://github.com/bottouch/hitbox_maker/assets/47953708/65dd23de-6dda-456a-8b0d-21755b154187)

Vous allez devoir modifier la variable MAIN_DIRECTORY_PATH pour la faire pointer vers votre fichier d'entente qui contient tout les sous dossiers avec toute les images.
Une fois executer, le logiciel va partir de la racine ( dans notre cas GOKU) , et faire chaque sous dossier, traiter toute les images, et ecrire un fichier data.json avec comme clef (1,2,3 etc... correspondant a chaque image)
