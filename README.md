# Dashboard Vaccination COVID-19

## Introduction
Bienvenue sur le README de notre Dashboard Vaccination COVID-19, une application Python conçue pour visualiser les données relatives aux stocks des doses de vaccins contre la COVID-19 en France.

## Objectif
L'objectif principal de cette application est de fournir une visualisation claire et interactive des données de vaccination. En utilisant les bibliothèques Dash et Plotly, notre dashboard offre une représentation graphique des statistiques, permettant ainsi une compréhension approfondie de la situation de la vaccination.

## Fonctionnalités
- Affichage interactif des données sous forme de tableau.
- Visualisation graphique des statistiques de vaccination via des histogrammes et des graphiques en cercle.

## Installation
1. Clonez le dépôt : `git clone https://github.com/ESIEECourses/Python_Project_Maguette_Julien.git`
2. Accédez au répertoire : `cd DashboardPython`
3. Créez et activez un environnement virtuel :
   - Sur Linux/Mac :
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Sur Windows :
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate
     ```
4. Installez les dépendances : `pip install -r requirements.txt`

## Utilisation
1. Activez votre environnement virtuel :
   - Sur Linux/Mac : `source venv/bin/activate`
   - Sur Windows : `.\venv\Scripts\activate`
2. Exécutez l'application : `python app.py`
3. Accédez au tableau de bord en ouvrant votre navigateur et en visitant http://127.0.0.1:8050/.


# Analyse des Données de Vaccination COVID-19

## Source des Données
Les données utilisées dans cette analyse proviennent du site officiel du gouvernement français et sont disponibles sur [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-stocks-des-doses-de-vaccins-contre-la-covid-19/). Elles incluent des informations sur les stocks des doses de vaccins contre la COVID-19 par département, type de vaccin, nombre de doses, et date.

## Objectifs de l'Analyse
Cette analyse se concentre sur plusieurs aspects clés, notamment :

1. **Répartition des Doses de Vaccins par Type :**
   - Visualisation de la répartition des doses de vaccins par type (Pfizer, Moderna, etc.).
   - Suivi des évolutions au fil du temps.

2. **Stocks des Doses par Département :**
   - Analyse des stocks des doses de vaccins par département.
   - Identification des départements avec les stocks les plus élevés.

3. **Tendances Temporelles :**
   - Visualisation des tendances temporelles du nombre de doses de vaccins administrées.

## Méthodologie
Les données utilisées dans cette analyse proviennent du fichier CSV disponible sur le site du gouvernement français ([data.gouv.fr](https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-stocks-des-doses-de-vaccins-contre-la-covid-19/)). Les informations extraites comprennent des détails sur les stocks des doses de vaccins contre la COVID-19 par département, type de vaccin, nombre de doses et date.

L'analyse des données a été réalisée en utilisant des techniques de traitement de données avec la bibliothèque pandas en Python. Les visualisations graphiques ont été générées par Plotly Express, offrant ainsi une représentation visuelle claire des statistiques de vaccination.

## Conclusions
Au cours du développement de notre application, en tant que débutants en Python ,Dash et Plotly, nous avons rencontré des défis majeurs, notamment l'apprentissage du langage Python, la compréhension de Dash, et l'intégration d'une carte interactive. Manipuler les données des stocks de vaccins s'est avérée complexe, nécessitant une maîtrise approfondie de pandas. Malgré ces difficultés, nous avons surmonté les obstacles en nous formant en ligne, consultant des ressources communautaires, et en adaptant notre code. Notamment, ce projet nous a permis de pratiquer le "peer programming" avec Diarra les weekends, renforçant ainsi notre collaboration à distance et notre compréhension mutuelle du code. En conclusion, bien que le projet ait présenté des défis, il a constitué une expérience précieuse d'apprentissage continu et de collaboration en équipe, contribuant significativement à notre développement professionnel.


## Perspectives Futures
L'intégration de données supplémentaires et l'exploration d'indicateurs spécifiques permettront d'affiner davantage l'analyse. Des mises à jour régulières du tableau de bord permettront de suivre les tendances au fil du temps, facilitant ainsi une adaptation continue des stratégies de vaccination en réponse à l'évolution de la situation.

## Auteurs
- Maguette Madiodiou Diagne 
- Mame Diarra Bousso Diakhaté 
