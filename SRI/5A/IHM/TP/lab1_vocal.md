# Une application dirigée à la voix
Nous souhaitons concevoir et réaliser une application **non-visuelle** (en *entrée* et en *sortie* incluant *parole* et éventuellement son -musique, messages enregistrés, etc.) permettant à un utilisateur **d’ajouter, retirer, manipuler des aliments affichés sur un écran afin de composer le contenu d’une assiette "gourmande" comprenant 2 boissons et 3 desserts au maximum**. (ex : café, jus d'orange, crème brûlée, profiteroles et fraises).

<img src="https://github.com/truillet/ups/blob/master/m2ihm/TP/ressources/triangle.png" align="center" width=400>

La disposition physique des desserts fait partie du problème !
Vous coderez votre application dans le **langage que <ins>vous désirez</ins>** :blush:.
**Il devra être possible d’effectuer toutes les actions demandées de manière purement vocale en entrée et en sortie**.

Afin de réaliser notre application multimédia, nous nous servirons prioritairement du **middleware (bus logiciel) [ivy](https://github.com/truillet/ivy/blob/master/README.md)**, support au *Bureau d’Etudes sur la multimodalité*.

**Nota** : Si vous travaillez sous Linux ou MacOS, il vous faudra trouver des solutions alternatives pour la reconnaissance (par exemple, [SpeechRecognition](https://pythonprogramminglanguage.com/speech-recognition), librairie python pour la reconnaissance vocale) et la synthèse vocale ([edgeTTS](https://github.com/rany2/edge-tts), [espeak-ng](https://github.com/espeak-ng/espeak-ng), [PyTTSx3](https://pypi.org/project/pyttsx3/) ou [MaryTTS](https://github.com/marytts/marytts)).

# Travail attendu de cette séance (2 heures)
Après avoir <ins>pris en main</ins> les [agents de reconnaissance **sra5**](https://github.com/truillet/ivy/blob/master/agents/doc_sra5.md) et de [synthèse vocale **ppilot5**](https://github.com/truillet/ivy/blob/master/agents/doc_ppilot5.md) fonctionnant avec le [bus logiciel **ivy**](https://github.com/truillet/ivy), l’objet de cette séance est :

1. de **définir la grammaire de reconnaissance** (commandes vocales ou langage *pseudo-naturel*) qui sera utilisée par votre application, gérer les résultats de la sortie sémantique (i.e. les concepts associés aux paroles prononcées) ainsi que le taux de confiance (Vous pouvez consulter la document [GrXML pour SAPI 5](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/Memo/GrXML.pdf) ou la [spécification grXML](https://www.w3.org/TR/speech-grammar)).
2. de **définir les retours (feedbacks) vocaux à synthétiser** et retours sonores utilisés par votre application (Vous pouvez consulter le [support SSML pour SAPI 5](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/Memo/ssml.pdf) ou la spécification [SSML - Speech Synthesis Markup Language](https://www.w3.org/TR/speech-synthesis11)). 
3. de **développer une application** d’affichage des plats à l’écran (en java, [Processing.org](https://www.processing.org) (voir [le dessert vocal](./ressources/dessert_vocal.zip) pour un exemple), python ... ou un autre langage).
5. et enfin **développer le contrôleur de dialogue** à **l’aide d’une machine à états** (qui peut être soit séparée, soit incluse dans l’application d’affichage de la forme). Le contrôleur s’appuiera sur un échange de messages [ivy](https://github.com/truillet/ivy/blob/master/README.md) avec *a minima* les modules de reconnaissance et de synthèse vocale.

A la fin de la séance, vous aurez produit un **prototype haute-fidélité testable** du système demandé. 

## Outils disponibles
* [sra5](https://github.com/truillet/ivy/blob/master/agents/sra5.zip), agent de reconnaissance vocale (prend en compte le format [GrXML](https://www.w3.org/TR/speech-grammar)
*	[ppilot5](https://github.com/truillet/ivy/blob/master/agents/doc_ppilot5.md), agent ivy de synthèse vocale (prend en compte le format [SSML](https://www.w3.org/TR/speech-synthesis11)
*	[Braille_display](./ressources/Braille_display.zip), agent ivy simulant une plage braille 10 points braille
*	le [visionneur ivy](https://github.com/truillet/ivy/blob/master/lib/visionneur_1_2.zip)
*	Le [middleware ivy](https://github.com/truillet/ivy)

