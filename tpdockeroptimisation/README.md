Premier build de l'image

Temps : [+] Building 30.4s (12/12) FINISHED
Remarque : durée assez longue et peut être optimisé

1 - Premier changement : Image plus légère

J'ai choisi une image de base plus légère de Node pour l'image (une version slim).

Temps : [+] Building 62.9s (13/13) FINISHED  
Remarque : Il n'y a pas eu une amélioration du temps de build car le choix de l'image représente la première layer
et donc on est obligé de refaire les layers qui suivent

2 - Ignorer node_modules

Ajout d'un fichier .dockerignore et mettre le dossier node_modules

Temps : [+] Building 60.5s (11/11) FINISHED 
Remarque : amélioration très minime

3 - Multi-stage

On compile dans une étape, on ne copie que le résultat dans l'image finale.

Temps : [+] Building 22.6s (15/15) FINISHED 
Remarque : diminution conséquante du temps de build grâce au multi-stage

4 - Cache des Layes

Temps : [+] Building 18.9s (17/17) FINISHED 
Remarque : quelques secondes de gagnées  