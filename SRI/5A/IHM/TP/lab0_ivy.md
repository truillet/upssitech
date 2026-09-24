# Démarrer avec le [middleware ivy](https://github.com/truillet/ivy)
## Introduction
Ivy est un bus logiciel [middleware] (https://www.eei.cena.fr/products/ivy) conçu à la DTI R&D (ex CENA)
dans le but de connecter d’une manière extrêmement simple des applications interactives ou pas en elles écrites avec différents langages et fonctionnant sur différentes machines ou plates-formes.

Il s’agit d’un modèle de communication compatible avec la programmation événementielle classique des interfaces graphiques. En un sens, ce bus logiciel implémente une approche multi-agents : les agents apparaissent, émettent des messages et en reçoivent, les traitent puis quittent le bus sans bloquer les autres agents présents. Ivy vise principalement à faciliter le développement rapide de nouveaux agents, et à en contrôler une collection dynamique.

Par opposition à certains autres bus logiciels, ivy ne se fonde pas sur un serveur central ou un annuaire qui permet de *router* les demandes d’un agent. Au lancement, tous les agents se présentent à un point de rendez-vous, le reste
est transparent pour le programmeur !

En  fait,  le  rôle  d’ivy  est  de  définir  principalement  une  convention  de  communication  entre  processus,  mise  en application grâce  à  une  collection  de  bibliothèques.  Les  messages sont  échangés  sous  une  forme textuelle et  la sélection des messages récupérés ou non par les agents est basée sur les expressions rationnelles (**regex** en anglais ; famille de notations compactes et puissantes pour décrire certains ensembles de chaînes de caractères).

### A quoi cela peut-il bien servir ?
Bien que limité à des échanges de messages textuels, ce principe permet de prototyper très rapidement (en ré-utilisant des agents déjà développés) voire de concevoir des systèmes adaptés spécifiquement aux besoins d’une personne, tout cela indépendamment du système.

Par exemple, pour un système qui aurait à afficher du texte dans une fenêtre graphique, on peut très facilement remplacer cet affichage par un synthétiseur vocal sans faire aucun changement au cœur du système, qui se contenterait d’envoyer sur le bus de l’information à donner aux utilisateurs.

En résumé :
1. ivy  n’est  qu’une  extension  de  la  programmation  événementielle  utilisant  TCP/IP  comme  vecteur  de
transport des événements
2. ce protocole peut être bien évidemment utilisé en complément d’autres protocoles (exemple : protocole http ; rtp pour la vidéo, CORBA pour l’échange d’objets, ...)
3. sa puissance (et sa faiblesse) réside(nt) dans la simplicité de la mise en œuvre. Attention néanmoins de ne pas négliger l’aspect conception du protocole d’échange des messages !

Les bibliothèques sont disponibles sur différents systèmes d’exploitation (Sun Solaris, Linux, Windows, Mac OS, Android, ...) pour plusieurs langages de programmation (Ada, C, C++, C#, Java, Perl, Perl-Tk, O-Caml, Python, Processing.org, Tcl, Tcl-Tk, VBA, ...).

### Fonctionnement
Quel que soit le langage utilisé, les principes de fonctionnement restent les mêmes :
1. **Création d’un nouvel acteur du bus**. Cela revient ici à allouer de la mémoire pour l’objet qui va se connecter au bus.
2. **Connexion de l’agent au bus**. Le bus ivy se connecte sur un port d’une adresse IP (ou de broadcast) du réseau local : c’est le point de rendez-vous de tous les agents qui veulent interagir entre eux.
3. **Envoi / réception des messages** (par un mécanisme d’abonnement). L’envoi de messages est extrêmement simple : il suffit de préparer la chaîne alphanumérique de données que l’on souhaite diffuser puis on active la fonction *send* associée à l’objet bus créé précédemment. Pour recevoir des messages du bus, il est nécessaire de s’abonner (fonction *bind*) à des *patrons* de messages  qui  permettront  l’activation  d’une  fonction de callback qui traitera le message reçu.
4. **Fermeture de la connexion et destruction de l’agent**

*Nota* : L’utilisation d’ivy implique l’utilisation de la pile de protocoles tcp/ip.

## Utiliser et développer avec ivy
### Etape 1 - charger les outils et configurer son environnement
Installer 
```
pipx install ivy-python
```

Téléchargez les deux agents *ivy* suivants (windows) :
* probe


Téléchargez les deux agents *ivy* suivants (linux / macOS) :
* probe


### Etape 2 - Vérifier la connexion entre agents
Depuis le Visionneur, envoyez le message suivant :

```
ppilot5 Say=bonjour tout le monde
```

### Etape 3 - créer son propre agent

```

```

#### Envoyer un message sur ivy

### Recevoir et traiter les messages reçus

## Exercices
### Maîtriser les expressions régulières et en faire une messagerie
L’objectif  du  premier  exercice  est  d’écrire  des  expressions  régulières  qui  pourront  être  utilisées  dans  vos développements ivy.

Vous testerez vos essais avec l’outil *Probe* Vous lancerez deux instances de Probe et testerez vos solutions en ajoutant des regex.

Soit une application X qui émet des messages du style : 
```
X time=1200 receiver=Y msg=blablabla
```

* Quelle serait l’expression régulière si :
  * Vous voulez récupérer seulement le nom du récepteur (champ receiver du message)
  * Vous voulez récupérer le nom du récepteur et le message (champ msg)
  * Tous les champs ?
* Supposons maintenant que des champs optionnels peuvent s’ajouter en fin de message : comment faire pour les récupérer et les traiter ?
* Quels seraient les avantages et inconvénients si on s’abonnait à "^(.*)" (tous les messages) ?
* Quel est, selon vous les avantages/inconvénients de structurer un message ivy ?

Développez maintenant un agent ivy permettant :
* D’envoyer un message à l’ensemble des personnes connectées sur la messagerie
* De recevoir et d’afficher les messages envoyés par les autres clients de la messagerie instantanée
* *(optionnel)* D’envoyer un message à une personne particulière connectée (en message privé)

*Nota :* pensez que chaque client doit avoir un nom particulier pour pouvoir recevoir des messages privés !

### Interagir avec d’autres langages
Tout d’abord, téléchargez le fichier xxx à l’adresse :

* Réécrivez  votre  agent  ivy  de  messagerie  (cf.  6.1)  afin  de  proposer  une  interface  « innovante »  de  votre messagerie.

### Réutiliser des agents précédemment développés
Sur https://github.com/truillet/xx

* Récupérez l’agent xxx
* Créez maintenant un petit dictionnaire de reconnaissance de gestes permettant de reconnaître un rectangle

* Utilisez cet agent (en lançant Icarivy.bat)
* A l’aide de l’outil de votre choix, étudiez la forme des messages envoyés par ICAR.
* Déduisez-en  une  expression  régulière  qui  vous  permettra  de  développer  une  application  (Traceur) permettant d’afficher dans un Panel la forme reconnue.

### vos propres applications ...
Maintenant, il ne reste qu’à concevoir et prototyper vos propres applications multimédia et/ou multimodales ! Le principe général est d’utiliser le langage le plus approprié pour chaque module afin de développer des prototypes haute-fidélité le plus rapidement possible.

Réutilisez, mixez, développez des agents réutilisables et le tour est joué !

### adresses utiles
* https://
