# Interaction Humain-Machine Multimodale / Multimodal Human-Machine Interaction

## Préambule / Preamble - ivy middleware
Les deux premiers sujets de travaux pratiques ont pour objectif de concevoir un système multimodal en entrée qui sera développé dans les trois suivants. Le dernier sujet traite de la multimodalité en sortie et de transmodalité (passage d'une modalité vers une ou plusieurs "équivalentes").
*The aim of the first two practical topics is to design an input multimodal system, which will be developed in the next three. The last topic deals with multimodal output and transmodality (switching from one modality to one or more "equivalent" ones).*

* [ivy presentation v 2.8 (FR)](https://github.com/truillet/ivy/blob/master/doc/C_ivy_2.8.pdf) (2025) / [ivy presentation v. 2.5 (EN)](https://github.com/truillet/upssitech/blob/master/SRI/5A/ID/Cours/C_ivy_2.5en.pdf) (2021)
* **Comment utiliser ivy / How to use ivy** - [ivy](https://github.com/truillet/upssitech/blob/master/SRI/5A/ID/TP/TP_ivy.3.5.pdf) (2022)
* **repository ivy** : [Github ivy](https://github.com/truillet/ivy/blob/master/README.md)  

## Interaction vocale / vocal interaction
* **TP1/Tutorial 1** - [Interaction vocale](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/lab1_vocal.md) (2025)
   * **Les outils utilisés dans le TP / tools used in this tutorial** : Agent de reconnaissance vocale / Speech Recognizer agent [sra5](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Code/sra5.zip), agent de synthèse vocale / speech Synthesis agent [ppilot5 v 3.3](https://github.com/truillet/ivy/blob/master/agents/ppilot5_3.3.zip), outil de supervision ivy / ivy monitoring tool [Probe](https://github.com/truillet/ivy/blob/master/code/Probe.zip) ou / or [visionneur](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Outils/visionneur_1_2.zip)
  * **[GrXML pour SAPI 5](https://github.com/truillet/upssitech/blob/master/SRI/3A/IHM/Memo/GrXML.pdf)**
  * **[SSML pour SAPI 5](https://github.com/truillet/upssitech/blob/master/SRI/3A/IHM/Memo/ssml.pdf)**
  
_Exemple de code Processing permettant l'affichage de la reconnaissance vocale et l'envoi du résultat vers la synthèse vocale / Example of Processing code allowing the text ouptut of speech recognition and sending the result to TTS_ : **[dessert](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Code/dessert.zip)**

## Interaction gestuelle / gesture interaction
* **TP2/Tutorial 2** - [Interaction gestuelle](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/TP2_InteractionGestuelle.pdf) (2024) / [Gesture Interaction](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/T2_gesture_interaction.pdf) (2023)

_Exemple de code Processing permettant l'enregistrement de formes dessinées à l'écran / Example of Processing code for recording shapes drawn on the screen_ : **[Enregistrement Forme](https://github.com/truillet/upssitech/blob/master/SRI/3A/IHM/TP/Code/Enregistrement_Forme.zip)**

_Autres ressources / Other resources_
   * **OneDollarIvy** (implémentation de l'algorithme du [$1 Recognizer](http://faculty.washington.edu/wobbrock/pubs/uist-07.01.pdf)) [code source](https://github.com/truillet/OneDollarIvy)
   * **ICAR** (implémentation de l'algorithme de [Rubine](http://reports-archive.adm.cs.cmu.edu/anon/itc/CMU-ITC-099.pdf)) [code source](https://github.com/truillet/icar), [fichier jar](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Outils/icar.1.2.zip) et [documentation](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Outils/icar.pdf)
  * **[$N Recognizer](https://depts.washington.edu/acelab/proj/dollar/ndollar.html)**

_Un peu d'Histoire  / A bit of History_
* [PalmOs et Graffiti](https://designobserver.com/feature/interface-runes/35108)
<img src="https://github.com/truillet/upssitech/blob/master/SRI/3A/IHM/ressources/Palm_Graffiti_gestures.png" height=250 alt="Graffiti gestures">
  
## Fusion Multimodale / Multimodal Fusion
* **TP3-5/Tutorial 3 to 5** - [Moteur de Fusion](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/TP3-5_Projet_Multimodal.pdf) (2024) / [Multimodal Engine](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/T3-5_multimodal_interaction.pdf) (2023)

_Exemple de code Processing permettant la gestion de formes géométriques / Example of Processing code for rmanipulating different shapes_ : **[Palette](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Code/Palette.zip)**

[<img src="https://img.youtube.com/vi/RyBEUyEtxQo/0.jpg" width=250 alt="Put That There">](https://youtu.be/RyBEUyEtxQo)

  * [R. Bolt, "Put-That-There": Voice and Gesture at the Graphics Interface, ACM SIGGRAPH Computer Graphics, Volume 14, Issue 3
Pages 262 - 270](https://doi.org/10.1145/965105.807503) et [R. Bolt, Reflexion on ... "Put-That-There": Voice and Gesture at the Graphics Interface](
https://github.com/truillet/upssitech/blob/master/SRI/3A/IHM/ressources/Bolt_1998_-_Reflections_on_Put-That-There.pdf)
  * [Sh. Oviatt, Ten Myths on Multimodal Interaction, Communication of the ACM, volume 42, Issue 11, November 1999](https://dl.acm.org/doi/10.1145/319382.319398)

## Fission Multimodale / Multimodal Fission
* **TP6/Tutorial 6** - [Multimodalité en sortie](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/lab6_multimodalite.md) (2025)

* **Les outils utilisés dans le TP / tools used in this tutorial** : agent de synthèse vocale / speech Synthesis agent [ppilot5 v 3.3](https://github.com/truillet/ivy/blob/master/agents/ppilot5_3.3.zip), agent d'affichage braille / braille display agent [Braille_display](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Code/Braille_display.zip), outil de supervision ivy / ivy monitoring tool [Probe](https://github.com/truillet/ivy/blob/master/code/Probe.zip) ou / or [visionneur](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/TP/Outils/visionneur_1_2.zip)
  * **[Speech Synthesis Markup Language - SSML](https://www.w3.org/TR/speech-synthesis11)** et **[support SSML pour SAPI 5](https://github.com/truillet/upssitech/blob/master/SRI/5A/IHM/Memo/ssml.pdf)**
  * autres liens "intéressants"
    * [seeing with sound](https://www.seeingwithsound.com/webvoice/webvoice.htm) : un exemple de transmodalité 
    * [Renault 25 et TTS](https://www.dailymotion.com/video/x2vt9b)
