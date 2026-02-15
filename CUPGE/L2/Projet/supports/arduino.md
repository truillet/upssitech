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
5. Lors de la première utilisation, il faut configurer la version de votre carte et le numéro de port série. Pour ce faire, aller dans le menu ``Outils`` puis successivement ``Carte`` pour configurer le type de votre plaque arduino et ``Port Série`` pour le numéro de port (choisissez le numéro de port préalablement donné lors de l’installation du pilote)

**Nous pouvons commencer à travailler**. Nous installerons plus tard de nouvelles librairies pour contrôler **arduino** et d'autres logiciels (comme [Fritzing](https://fritzing.org/download)) pour se rappeler de nos montages arduino facilement.

# 1. introduction
## 1.1 [Histoire d’arduino](http://spectrum.ieee.org/geek-life/hands-on/the-making-of-arduino)
C’est à Ivrea en Italie, terres du roi **Arduin** (Arduino en italien) vers l’an mil que commence l’histoire de cette plateforme électronique. Créé en 2005 comme outil pour les étudiants de l’[Interaction Design Institute d’Ivrea](https://interactionivrea.org/en/index.asp), arduino est devenu en moins de 8 ans le projet de plus influent de l’électronique moderne.

Sous licence [Creative Commons](https://creativecommons.org) (les plans sont libres), arduino peut permettre d’effectuer des tâches extrêmement diversifiées comme des tâches domotique ou robotique.

Il existe de nombreux matériels compatibles Arduino comme [ESP32](https://www.espressif.com/en/products/socs/esp32) ou encore [teensy](https://www.pjrc.com/teensy), ...

## 1.2 IDE arduino
L’IDE (Environnement de Développement) permet de préparer ses programmes (appelés *sketch*), vérifier la syntaxe et télécharger le programme sur la plateforme arduino. Il y a plusieurs manières de programmer pour arduino : la première est d'utiliser le langage C(++) et la seconde d'utiliser python (pour certaines plateformes) avec micropython ou circuitpython.

Le programme arduino est divisé en deux parties (fonctions) par défaut :
* ``setup()`` qui initialise un certain nombre de valeurs
* ``loop()`` qui correspond à une boucle sans fin et qui exécute le code contenu dans la fonction.

## un premier exemple : blink
Prenons un exemple. Ouvrons le programme ``blink`` situé dans ``Fichier | Exemples | 01.Basics | Blink``. Le programme va faire clignoter une led que nous allons placer sur le pin 13. 

# 2. A vous de jouer !!!
## 2.1 une led comme capteur de lumière
Nous allons utiliser une led infrarouge pour allumer un éteindre une led branchée sur le pin 13 (*Le pin 13 possède une résistance interne de 220 ohms*).

Branchez la led infrarouge sur l’entrée analogique ``A0`` et ``GND``.

Ecrire un programme qui lit une valeur sur l’entrée ``A0`` et allume la led sur le pin 13 si une valeur de seuil est dépassée.

## 2.2 un capteur de température
Utilisons maintenant un module de température [KY-013](https://sensorkit.joy-it.net/en/sensors/ky-013)

Câblez votre capteur et codez la fonction de transformation qui permettra de renvoyer la valeur de température en degrés Celsius sur la liaison série en fonction des valeurs lues sur le pin analogique.

## 2.3 feux tricolores
Un feu tricolore peut être dans l’état rouge, orange, vert. Dans le cas classique, le feu est successivement vert, puis orange, puis rouge, puis de nouveau vert, etc.

Dans ce cas, il reste 6 secondes au vert, 1 seconde à l'orange, et 7 secondes au rouge (histoire de ne pas attendre trop longtemps ☺)

Déterminez le montage électronique (**Attention** : pensez à utiliser une résistance de 220 ohms si vous utilisez un autre pin que le pin 13), codez et testez !

**Nota** : vous pouvez utiliser le logiciel [Fritzing](http://fritzing.org/download) pour dessiner et sauver votre montage !

## 2.4 changement d’état via un bouton physique (feux … suite)
Modifiez votre montage et votre code de telle manière que l’appui sur un bouton physique permette de changer de l’état nominal à l’état clignotant (le feu orange clignote à une fréquence de clignotement toutes les deux secondes) et inversement.

## 2.5 contrôle de moteurs (feux … encore)
Modifiez encore votre montage afin d’intégrer une barrière (ouverte/fermée) à partir d’un servomoteur sur une des intersections.

## 2.6 contrôle par le PC (feux … toujours)
Modifiez encore le résultat de telle sorte qu’un envoi de données par la liaison série (un caractère par exemple) à l’arduino permette ce changement d’état (contrôle par le PC).

