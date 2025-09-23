# TD 3 : Les aventures de π / méthodes de calcul d’intégrales

## Calcul de π
Le nombre π est sans doute l’entité mathématique la plus connue de par le monde. Apparu dès l’Antiquité de manière intuitive en tant que rapport du périmètre d’un cercle sur son diamètre, il n’a cessé de susciter l’intérêt  en  mathématiques.  Mais  c’est  Archimède  (287-212  avant  J.C.)  qui  le  premier  se  pencha réellement sur la question.
Dans son écrit De la mesure du cercle, il commence par démontrer qu’il existe une unique constante π telle que l’on ait A=πR² et P=2πR, où A et P sont respectivement l’aire et le périmètre du cercle de rayon R.

Ce sont ces fameuses décimales qui aujourd’hui font tout l’intérêt de ce nombre. Nous allons donc étudier diverses méthodes et formules pour approcher ce nombre π.

Vous allez tout d’abord écrire une série de fonctions sous GNU Octave permettant de calculer une valeur approchée de π suivant un nombre n d’itérations souhaitées.

### Produit infini de Viète (1540-1603)

$U_0=1/sqrt{2}$

$`\U_n=sqrt(1/2+1/2U_(n-1)\`$


### Produit infini de Wallis (1606-1703)

### Formule d’Euler (1707-1783)

### La méthode de Monte-Carlo
Le terme de *méthode de Monte-Carlo* désigne toute méthode visant à calculer une valeur numérique en utilisant des procédés aléatoires, c’est-à-dire en utilisant des techniques probabilistes. Le nom de ces méthodes, qui fait allusion aux jeux de hasard pratiqués à Monte-Carlo, a été proposé par l’équipe du physicien Nicholas Metropolis.
Les méthodes de Monte-Carlo sont particulièrement utilisées pour calculer des intégrales (en particulier, pour calculer des surfaces et des volumes). Elles sont également couramment utilisées en physique des particules, où des simulations probabilistes permettent d'estimer la forme d’un signal ou la sensibilité d’un détecteur.

L’exemple suivant est un classique de l’usage de la méthode de Monte-Carlo. Soit une zone rectangulaire
ou carrée dont les côtés sont de longueur connue. Au sein de cette aire se trouve un lac dont la superficie
est  inconnue.  Grâce  aux  mesures  des  côtés  de  la  zone,  on  connaît  l’aire  du  rectangle.
Pour trouver l’aire du lac, on demande à une armée de tirer « x » coups de canon de manière aléatoire
sur cette zone. On compte ensuite le nombre « n » de boulets qui sont restés sur le terrain ; on peut ainsi
déterminer le nombre de boulets qui sont tombés dans le lac : x-n. Il suffit ensuite d’établir un rapport
entre les différentes valeurs pour trouver l’aire finale.

Soit un point M de coordonnées (x, y), où 0<x<1 et 0<y<1.

On tire aléatoirement les valeurs de x et y. Le point M appartient au disque de centre (0,0) de rayon
1 si et seulement si x²+y²= 1.

La probabilité que le point M appartienne au disque est alors de π/4. En faisant le rapport du nombre
de points dans le disque au nombre de tirages, on obtient une approximation du nombre π si le nombre
de tirages est grand.

## Intégrales et méthodes de calcul
Soit f une fonction continue sur [a,b], dans les exercices qui suivent, il s’agira d’approcher l’intégrale :

### Méthode des rectangles
Dans la méthode dite des rectangles, on a le choix entre trois techniques :

1. on  fait  coïncider  le  sommet  haut  gauche  du  rectangle  avec  la  courbe :  c’est  la  méthode  des rectangles à gauche,
2.  on  fait  coïncider  le  sommet  haut  droit  du  rectangle  avec  la  courbe :  c’est  la  méthode  des rectangles à droite,
3.  on fait coïncider le milieu du côté haut du rectangle avec la courbe : c’est la méthode du point milieu

On définit le pas d’approximation :

où n est le nombre de rectangles avec lesquels nous allons « paver » l’aire à calculer.


On définit ainsi :

Avec la méthode du point milieu, l’aire se calcule de la manière suivante :


Ecrire une fonction GNU Octave integration_rectangles qui utilise la méthode des rectangles.

### Méthode des trapèzes
La méthode des trapèzes est à peu près similaire à la méthode précédente mais on utilise maintenant
des trapèzes pour « paver » l’aire afin d’être plus précis.

Comme plus haut, l’intervalle [a,b] est partagé en n petits trapèzes de largeur h = (b-a)/n. Nous savons ainsi que l’aire de chaque petit trapèze est Ai = (h/2)*(f(a+ih) + f(a+(i-1)h)).
Nous obtenons alors l’aire recherchée en sommant l’aire de tous les trapèzes entre a et b, ce qui nous donne (vous pouvez vérifier !) :

Ecrire une fonction GNU Octave integration_trapezes qui utilise la méthode des trapèzes.

### Méthode de Monte-Carlo
Soit une fonction f(x) définie sur l’intervalle [a,b]. On définit un rectangle de longueur b-a (axe des abscisses) et de largeur z (axe des ordonnées) telle que z soit supérieur à tout point de la courbe f(x). On génère (n+1)2 points espacés régulièrement, avec des pas notés px et py respectivement suivant l’axe des abscisses et des ordonnées. Pour chaque abscisse xi, on compare chaque valeur yi des points associés à cette abscisse avec la valeur de f(x). Chaque fois que y<f(x), on incrémente la valeur d’un compteur C. On calcule ensuite le rapport R entre le nombre de points compris sous la courbe et  le  nombre  total  de  points.  La  valeur  approchée  I  de  l’intégrale  est  donnée  par  la  relation  I  =

Ecrire une fonction octave qui permet d’estimer l’intégrale de la fonction f(x).


