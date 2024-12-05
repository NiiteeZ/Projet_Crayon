# Pencil Manufacturing Project 

_Author 1_ : Sylvain ETANGSALE <br>
_Author 2_ : Jean-Luc BITOUMBOU-BIBOKA <br>
_Version_ : 08/11/2024

Ce projet git est ..

## 1. Installation et démarrage 
### 1.0 - Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine : 
- Python 3
- Pip
- Git
- Venv

### 1.1 - Cloner le dépôt
- Clonez le dépôt Git du projet en local :
```bash
git clone https://github.com/NiiteeZ/Projet_Crayon.git
```
### 1.2 - Se placer dans le dossier
```bash
cd Projet_crayon
```
### 1.3 - Configurer l'environnement virtuel
- Créez un environnement virtuel :
```bash
python3 -m venv .venv
echo .venv >> .gitignore
```
- Activez l'environnement virtuel celon votre machine :
```bash
source .venv/bin/activate  #Linux

.venv\Scripts\activate #Windows
```
### 1.4 - Installer les dépendances nécessaires
- Installez les packages requis pour le projet :
```bash
pip install -U pip
pip install django
```
## 2. Lancement du serveur Django
- Executez les commandes suivantes pour préparer et lancer le serveur :
```bash
python ./manage.py makemigrations
python ./manage.py migrate
```
- Créez un user et mot de passe pour le serveur :
```bash
python ./manage.py createsuperuser
```
__METTRE IMAGES DU TERMINAL POUR MONTRER RESULTAT ATTENDU__

- Lancer le serveur local :
```bash
python ./manage.py runserver
```
- Ouvrez le lien suivant avec un navigateur : 
```bash
http://localhost:8000/admin/
```