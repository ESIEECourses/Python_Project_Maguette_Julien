# DASHBOARD Traitement des données COVID 

# Introduction
## Mode opératoire
### Difficultés renconrées
### Ressources utilisées
# USER GUIDE
## Requirements
## Lancement de l'aplication
### Sous Windows
### Sous Linux 
### Structure des pages
## GUIDE DU DEVELOPPEUR
### Technologies
### Environnement de développement
### Sous Windows
### Sous Linux
### Structure du code


I. RAPPORT D'ANALYSE
I.1 Introduction
I.2 Mode opératoire
I.3 Difficultés rencontrées
I.4 Ressources utilisées
II. USER GUIDE
II.1 Packages nécessaires
II.2 Lancer l'application
II.2.1 Sous Windows
II.2.2 Sous Linux
II.3 Structure des pages
III. DEVELOPER GUIDE
III.1 Technologies
III.2 Environnement de développement
III.2.1 Sous Windows
III.2.2 Sous Linux
III.3 Structure du code

Ressources utilisées
Le fichier de données utilisé provient de ce site : https://www.gapminder.org/data/

USER GUIDE

Packages nécessaires
Il est essentiel d'avoir installer Anaconda au préalable pour un OS Windows, le téléchargement se fait via ce site : https://www.anaconda.com/products/individual/ .
Avant de commencer les installations des packages, il faut lancer la commande : conda update --all
Cette commande permet de mettre à jour les packages conda et évite l'apparition de certaines erreurs lors de l'installation de certains packages.



Nom du package
Commande d'installation




Sous Windows



Plotly express
pip install plotly --upgrade


Pandas
conda install --channel conda-forge pandas


Geopandas
conda install --channel conda-forge geopandas


Dash
conda install --channel conda-forge dash


Dash_bootstrap_components
conda install -c conda-forge dash-bootstrap-components


Sous Linux



Plotly express
python3 -m pip install plotly-express


Pandas
python3 -m pip install pandas


Geopandas
python3 -m pip install geopandas


Dash
python3 -m pip install dash


Dash_bootstrap_components
python3 -m pip install dash-bootstrap-components




Lancer l'application

Sous Windows
Tout d'abord, il faut installer Python. Pour cela, téléchargez l'installeur Windows disponible sur ce site : https://www.python.org/downloads/release/python-387/ .
Une fois Python installé, on peut lancer l'application, ouvrez alors un terminal. Il suffit de chercher « Invite de commandes » dans la barre de recherche Windows. Il est aussi possible d'appuyer sur les touches Windows et R, de taper « cmd » puis appuyez sur OK.
Il faut ensuite se positionner dans le dossier où se trouve les fichiers sources. Pour cela, utilisez la commande « cd cheminVersLeDossier ». Si le dossier se trouve sur un autre disque (le disque est indiqué par la première lettre du chemin, il s'agit habituellement du disque C), il faut changer de disque en faisant la commande « lettre: ».
Une fois dans le bon dossier, faites la commande « dir », vous devriez voir apparaitre des noms de fichiers et de dossiers, dont main.py.
Si c'est le cas, vous pouvez écrire la commande « python main.py ». Si au contraire, le nom du fichier n'apparait pas cela signifie que vous n'êtes pas dans le bon dossier.
Pour accéder au dashboard, il faut ouvrir une page internet et taper l'adresse qui s'est affichée dans le terminal.
Exemple :

Ici, l'adresse à afficher est 127.0.0.1:8085

Sous Linux
Tout d'abord, il faut que Python soit installé sur votre poste. Vous pouvez vérifier que Python est bien installé avec la commande « python3 ». Sinon, ouvrez un terminal.
Il suffit de chercher « Terminal » dans les applications, puis exécutez la commande « apt-get install python3 » .
Une fois Python installé, on peut lancer l'application, toujours dans le terminal, il faut se positionner dans le dossier où se trouve les fichiers sources. Pour cela,
utilisez la commande « cd cheminVersLeDossier ».
Une fois dans le bon dossier, faites la commande « dir », vous devriez voir apparaitre des noms de fichiers et de dossiers, dont main.py.
Si c'est le cas, vous pouvez écrire la commande « python3 main.py ». Si au contraire, le nom du fichier n'apparait pas cela signifie que vous n'êtes pas dans le bon dossier.
Pour accéder au dashboard, il faut ouvrir une page internet et taper l'adresse qui s'est affichée dans le terminal.
Exemple :

Ici, l'adresse à afficher est 127.0.0.1:8050

Structure des pages
L'application est divisée en deux pages principales.
Sur la première page, il est possible de voir deux cartes du monde. Il est possible de choisir l'indicateur à afficher sur les cartes grâce à la liste déroulante.




# Python_Project_Maguette_Julien
Projet Python de Dashboard sur un sujet d'intérêt public

Pour activer l'environnement virtuel la commande : 
.\venv\Scripts\activate

lien d'obtention des données 
https://covidtracker.fr/pip


ctrl alt s python interpreter settings (c)
requirements 
python 3.12.0
pandas 2.1.3
numpy 
selenium 0.14.0
chromedriver 

