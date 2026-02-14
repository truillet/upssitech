# Python et micro-électronique
Depuis une dizaine d'années, python a envahi la micro-électroniques et peut s'exécuter sur de nombreux dispositifs : ESP32, Raspberry Pico, etc. 
Deux projets ont émergé ces dernières années : *microPython* et *circuitpython 

## micropython <img src="https://github.com/truillet/upssitech/blob/master/CUPGE/L2/Projet/supports/images/micropython.jpg" width=50>
[MicroPython](https://micropython.org) est une implémentation de Python3 qui inclut un sous-ensemble des librairies standard du langage fonctionnant sur des micro-contrôleurs et dans des environnements contraints.

**micropython** est un portage du langage python avec 
* un portage complet des mot-clés, des objets et fonctions built_in
* un portage de modules standards (comme ```time, sys, os, io, math, ...```)
* des modules spécifiques aux micro-contrôleurs
* des librairies permettant l'accès aux capteurs/effecteurs
* des modules spécifiques à la plateforme matérielle utilisée

### installer micropython
Le téléchargement du *firmware* de **micropython** est la première étape pour commencer à utiliser python sur votre micro-contrôleur.
1. Connectez votre appareil : Utilisez un câble USB pour connecter votre microcontrôleur à votre ordinateur.
2. visitez le centre de [téléchargement](https://micropython.org/download) de micropython
3. sélectionner votre appareil et télécharger le *firmware*
4. installer le *firwmare* (via l'[IDE Thonny](https://thonny.org) par exemple)

### Liens
* https://docs.sunfounder.com/projects/kepler-kit/fr/latest/pyproject/for_micropython_user.html

## circuit python <img src="https://github.com/truillet/upssitech/blob/master/CUPGE/L2/Projet/supports/images/circuitpython.png" width=50>
[circuitpython](https://circuitpython.org)
**circuit python** est un dérivé open-source de micropython porté par [Adafruit](https://www.adafruit.com)

### installer circuitpython
Le téléchargement du *firmware* de **circuitpython** est la première étape pour commencer à utiliser python sur votre micro-contrôleur.
1. Connectez votre appareil : Utilisez un câble USB pour connecter votre microcontrôleur à votre ordinateur.
2. visitez le centre de [téléchargement](https://circuitpython.org/downloads) de circuitpython
3. sélectionner votre appareil et télécharger le *firmware*
4. installer le *firwmare*

Sur les appareils avec support UF2 (comme le Raspberry Pi Pico), vous devrez entrer dans le mode bootloader avant d'installer CircuitPython. La plupart du temps, vous devez appuyer sur un bouton **boot** sur votre carte avant de connecter le câble USB. Reportez-vous à la documentation de votre appareil spécifique pour savoir comment entrer en mode bootloader et suivez les instructions


