# arduino 

## Préambule
Avant de commencer, il faut installer sur le poste de travail l’environnement de travail (IDE) [arduino](http://www.arduino.cc). Supposons que l’IDE soit installé sur le répertoire ``C:/langages``
Dans le cas contraire, il faut :
   * Télécharger le logiciel (version 2.3.7)
   * Créer deux répertoires sur ``C:/langages`` et sur ``C:/dev``
   * Décompresser l’archive téléchargée dans ``C:/langages/arduino-2.x.x`` (*où x.x représente le numéro de version*)

1. Brancher sur un port usb une plaque arduino et installer les pilotes (drivers) si nécessaire
2. Lancer l’IDE arduino en cliquant sur **arduino.exe** dans son répertoire
3. Dans le répertoire ``dev``, créer un répertoire ``arduino``
4. Modifier dans ``Fichier | Préférences`` l’emplacement du carnet de croquis vers ``C:/dev/arduino``. Appuyer sur ok et redémarrer **arduino.exe**

**Nous pouvons commencer à travailler**. Nous installerons plus tard de nouvelles librairies pour contrôler **arduino** et d'autres logiciels (comme [Fritzing](https://fritzing.org/download)) pour se rappeler de nos montages arduino facilement.

# 1. introduction
## 1.1 [Histoire d’arduino](http://spectrum.ieee.org/geek-life/hands-on/the-making-of-arduino/0)
C’est à Ivrea en Italie, terres du roi Arduin (Arduino en italien) vers l’an mil que commence l’histoire de cette plateforme électronique. Créé en 2005 comme outil pour les étudiants de l’Interaction Design Institute d’Ivrea, Arduino est devenu en moins de 8 ans le projet de plus influent de l’électronique moderne.

Sous licence [Creative Commons](https://creativecommons.org) (les plans sont libres), arduino peut permettre d’effectuer des tâches extrêmement diversifiées comme des tâches domotique ou robotique.

Il existe de nombreux matériels compatibles Arduino comme [ESP32](https://www.espressif.com/en/products/socs/esp32) ou encore [teensy](https://www.pjrc.com/teensy), ...


