# Travaux Dirigés - Lois Psycho-Physiques *(inspiré des TDs IHM du LRI)*

## 1. Loi de Fitts
*Le temps mis pour atteindre une cible est proportionnel à sa distance et inversement proportionnel à sa taille*

Mathématiquement, a loi de Fitts a été formulée de plusieurs manières, l’indice de difficulté été calculé par **log<sub>2</sub>(2D/d)** ou **log<sub>2</sub>(1 + D/d)**, formulation dite *de Shannon* proposée par Scott MacKenzie.

**Rappels** :
 * *Logarithme binaire* : log<sub>2</sub>(2n) = n
 * *Loi de Fitts :* T=a+bID avec *T : temps de pointage (en secondes)* et *ID = log<sub>2</sub>(2D/d)* (D : Distance à la cible, d : diamètre de la cible)

### 1.1. Expérimenter (en ligne)
Il existe de nombreux sites web qui permettent d’expérimenter et visualiser les résultats de la Loi de Fitts. Parmi ceux-ci, on peut citer : [Interactive Visualisation of Fitt's Law](http://www.simonwallner.at/ext/fitts), visualisation avec Javascript et D3.js) ou [Fitt's Law demonstration](https://fww.few.vu.nl/hci/interactive/fitts), démonstration en ligne et explications de la Loi.

### 1.2. Estimer
On considère quelques temps (en secondes) mesurés lors d’une expérimentation avec un dispositif particulier.
Pour ce dispositif, **déterminer** (grossièrement) les valeurs des constantes expérimentales **a** et **b** utilisées de la loi de Fitts.

| **d \ D** | **1.00** | **5.00** | **10.00** |
| --- | --- | --- | --- |
| **0.10** | 0.31 s | 0.45 s | 0.56 s |
| **0.50** | 0.13 s | 0.30 s | 0.38 s |
| **1.00** | 0.07 s | 0.252 s | 0.32 s |

| **D** | **1** | **1** | **1** | **5** | **5** | **5** | **10** | **10** | **10** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **d** | **0,1** | **0,5** | **1,0** | **0,1** | **0,5** | **1,0** | **0,1** | **0,5** | **1,0** |
| **log<sub>2</sub>(2D/d)** | 4,32 | 2 | 1 | 6,64 | 4,42 | 3,32 | 7,64 | 5,32 | 4,32 |

### 1.3. Prédire
Typiquement, la durée d’un clic souris est évaluée à **10 ms**, la largeur d’une icône à **1 cm**, la hauteur d’un menu à **0,7 cm** et sa largeur à **5 cm**.

On supposera le temps d’affichage comme étant **nul**. On prendra les valeurs suivantes pour **a** et **b** : **a=0** et **b=0,1**. (paramètres classiques de la loi de Fitts). Enfin, le curseur se situe à chaque opération au centre de l’écran (on prendra comme distance initiale entre le curseur souris et le centre du widget ≈ **20 cm**)

1. Evaluez le temps moyen pour la sélection d’une commande dans un menu unique à 25 entrées.
   On choisira de pointer la 13ème entrée.
2. Comparez le temps pour effectuer une opération par *drag-and-drop* et par la sélection d’une icône suivie de la sélection d’une commande dans un menu. (on prendra la taille de la fenêtre égale à **10 cm** et la distance entre les icônes égale à **20 cm**).
   Le curseur est positionné au départ sur l’icône à sélectionner.
3. Enfin, comparez le temps de pointage d’un item d’un [pie-menu](https://en.wikipedia.org/wiki/Pie_menu) à 4 entrées (rayon du menu = **3 cm**) et de la troisième entrée d’un menu « *surgissant* » (popup menu) à 4 entrées.
   Qu’en concluez-vous ? Quelles critiques pouvez-vous formuler ?

### 1.4. Des limites à la Loi de Fitts
Que se passe t’il quand :

1. On veut pointer une cible de **10 pixels de largeur** au milieu en haut de l’écran sur un écran **4000 x 4000** (sur un écran de **50 pouces** soit **127 cm** de diagonale).
   **Nota** : 1 pouce = 2,54 cm

   Le curseur est au centre de l’écran. En reprenant les paramètres estimés en (1), calculer le temps moyen pour atteindre la cible et calculer la distance « réelle » à parcourir
2. Et quand le rapport **2D/d > 1 000**
3  Que pouvez-vous en conclure ?

## 2. Loi de Hick-Hymann
*Le temps de décision est proportionnel au nombre d’alternatives proposées*

**Rappel** :
* *Loi de Hick* TR=a +blog<sub>2</sub>(n) avec TR : Temps de réaction, n : nombre d’alternatives (les paramètres a et b sont traditionnellement fixés pour un novice à **a=0** et **b=0,2**)

1. Calculez le temps moyen de décision dans un menu à *25 entrées*
2. Calculez le temps moyen de décision dans un menu à *4 entrées*
3. Calculez le temps moyen d’accès à l’item de menu défini en **1.3.3.** Quelle est votre conclusion ?

## 3. KLM - Keystroke Level Model
Keystroke-Level Model (KLM), proposé par [Card, Moran et Newell](https://www.taylorfrancis.com/books/mono/10.1201/9780203736166/psychology-human-computer-interaction-stuart-card) (1983), prédit le temps d’exécution d’une tâche à partir d’un scénario de tâche spécifiques. Il s’agit essentiellement d’énumérer la séquence d’actions au niveau des touches que l’utilisateur doit effectuer pour accomplir une tâche.

Il n’est pas nécessaire de disposer d’une maquette, KLM exige seulement que l’interface utilisateur soit spécifiée de manière suffisamment détaillée pour dicter la séquence des actions.

### A votre avis, quelle est la méthode la plus rapide pour effacer une partie de texte sous un éditeur standard ?

Pour répondre à cette question, *trois techniques sont envisagées* : soit vous vous placez à la fin du texte à supprimer et vous appuyez autant de fois que nécessaire la touche de suppression (**SUPPR**), soit vous sélectionnez l’ensemble du texte indésirable à supprimer avant d’appuyer (une fois) cette touche. Enfin, une fois le texte sélectionné, vous pouvez sélectionner l’item « *supprimer* » du menu « édition » de la barre de menus.

1. En vous appuyant sur le modèle KLM, estimez le temps nécessaire pour la suppression d’un texte de 3 caractères adjacents.
2. Faites de même pour une suppression de 10 caractères adjacents.
3. Les résultats obtenus sont-ils intuitifs ? Quels sont les limites de ces calculs ?

### Rappel : **KLM** introduit six opérateurs pour décrire l’exécution d’une tâche élémentaire

* **K** : « keystroking », frappe de touches du clavier ou de la souris – entre 0.08 et 1.20 s suivant l’expertise des utilisateurs – **0,2 s**
* **P** : *pointing*, désignation – entre 0,8 s et 1,5 s, **on prendra la valeur médiane 1,1 s**
* **H** : *homing*, rapatriement de la main – **0,4 s**
* **D** : *drawing*», action de dessiner – **0,9 n + 0,161** (n = nombre de segments tracés)
* **M** : *mental activity*, activité mentale – **1,35 s**
* **R** : *response time*, temps de réponse du système – **max (0, n-t)** – n = temps de traitement d’une commande par le système, t = temps exploité par l’utilisateur

Le temps d’exécution est la somme des temps passés à exécuter chaque classe d'opérateurs.

**Estimateur** : [KmlCalc](https://github.com/truillet/upssitech/blob/master/SRI/1A/TD/KlmCalc.exe) (application windows)

