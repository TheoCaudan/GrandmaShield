# Bienvenue dans le README du projet Mamie

## Le projet vient au départ de mon envie de résoudre une bonne fois pour toute les problèmes de ma mamie sur son ordinateur.J'ai donc pensé d'abord à son problème de doublons qu'elle génère sans faire exprès de façon plutôt conséquente à la longue.

### 1. DPL_Handler

Le DPL_Handler va simplement récupérer le hash de tous les fichiers dans le 
dossier spécifié et va les comparer puis supprimer les doublons identifiés.

## Après cela il fallait qu'elle retrouve ses fichiers facilement donc j'ai pensé à un outil automatique pour organiser ses fichiers sans qu'elle n'ai a reflechir où le trouver.

### 2. FILE_Organizer

Le FILE_Organizer va lui organiser les fichiers par type, on aurait pu le faire par date (la fonction existe il suffira d'ajouter la ligne : "organize_files_by_date" à la place de "organize_files_by_type" à la fin du fichier file_organizer.py), j'ai choisi par type parceque souvent elle me dit quel type c'est quand elle veut que je l'aide à chercher un fichier.
Tout d'abord il faudra renseigner au fichier file_organizer.py le path/to/your/directory le dossier que vous souhaitez ranger par type. 
Le programme va ouvrir le dossier, lister son contenu et regarder le type des fichiers presents puis les trier par type dans des dossiers nommé avec les types de dossier en majuscules parceque ma mamie a une mauvaise vue.

## Mais quand est-il du dossier de téléchargements ? On le sait tous c'est souvent le desordre, alors j'ai pensé à un outil simple pour nettoyer tout ça.

Le but est d'avoir un outil simple qui va vérifier depuis combien de temps un fichier est dans le dossier cible et va l'archiver où vous le souhaiter si il est jugé trop "vieux". Cela va permet d'avoir un dossier de téléchargements plus propre en attendant que je fasse un script pour ségréguer le contenu des archives et supprimer et/ou déplacer ce dernier.

## Pendant que j'y suis, étant étudiant en cybersecurite je vais le rendre un peu plus sécurisé son système à mamie.

