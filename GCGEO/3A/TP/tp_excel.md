# TP Excel
Objectifs de la séance : 
- découvrir l'environnement Excel
- appliquer les principaux outils de saisie et de mise en forme
- découvrir les notions de référence absolue et relative
- découvrir les outils de construction automatique d'une série arithmétique 


## Exercice 1 
Ouvrir le fichier notes.txt. Il contient une liste de notes en Mathématiques, Physique, Informatique et Anglais pour les étudiants dont le nom est situé en début de ligne.
Entrer ces notes dans une feuille de calcul Excel de nom *Notes.xlsx*».
Insérer une ligne en haut de la feuille et préciser l’intitulé de chaque discipline
Rajouter une colonne à droite, contenant la moyenne, en affectant le coefficient 4 pour les maths, 3 pour la physique, 2 pour l’informatique et 2 pour l’anglais (la moyenne doit apparaître au dixième de point près, en Gras et en couleur verte).

Créer une nouvelle feuille de nom *Alpha* qui reprend les données de « Notes » et classe les étudiants par ordre alphabétique (sous-menu Trier du menu Données)
Créer 2 feuilles de noms « Math » et « Ang » qui reprend les données de « Notes » et affichant les étudiants par note décroissante dans la matière et ordre alphabétique.
Créer une nouvelle feuille de nom « Class » qui reprend les données de « Notes » et ajouter une colonne affichant le rang, avant celle contenant le nom de l’étudiant, et qui donnera le classement de l’étudiant (pour cela on pourra utiliser la fonction ‘rang’).
On affichera au bas de cette feuille, les moyennes et les médianes de chaque matière et la moyenne générale.

A partir de la feuille « Class », créer une nouvelle feuille « Mentions », qui va faire apparaître les mentions des étudiants dans une colonne à droite de celle de la moyenne. On rappelle qu’au-dessous de 12, les étudiants ont la mention Passable, que la mention AB est accordée lorsque la moyenne générale est supérieure ou égale à 12 et inférieure à 14 et que la mention B est obtenue pour une moyenne allant de 14 à moins de 16, au-dessus de 16 les étudiants ont la mention TB. On utilisera la fonction logique SI du tableur Excel.

Dans une nouvelle feuille « Mentions2 », créer à partir de « Mentions », on utilisera le sous-menu Filtre du menu Données afin de ne faire apparaître que les mentions Bien (grâce à Filtre, on peut d’un simple clic faire apparaître toutes les mentions passable, AB, TB…).

Chercher dans les fonctions Excel celle(s) qui pourrai(en)t vous aider à tracer un graphique donnant pour chaque note le nombre d’occurrences rencontrées pour les mathématiques.

Utiliser la mise en forme conditionnelle dans le menu Format afin de faire apparaître en rouge toutes les notes inférieures à 8. Le format doit se modifier automatiquement si on modifie les notes.

## Exercice 2
Un câble acier de 2 m de longueur est soumis à un effort de traction variant de 0 et 1 500 daN. L'allongement delta L de ce câble est calculé par l'intermédiaire de la formule suivante :
avec :	F effort de traction
	L longueur du câble
	E = 210 000 MPa module d'élasticité de l'acier
	S = 7,57 cm2 section du câble

Créer une feuille sous Excel ayant le format du modèle présenté ci-dessous :
