# Bureau d’Etudes - un superviseur de capteurs réels et virtuels
*(A réaliser par groupe de 4 à 6)*

## Votre mission
Votre mission va être de créer, de gérer et de superviser un réseau de capteurs à partir de données *réelles locales* (température, pression, luminosité, taux d’humidité, détection d'images, ...) et à distance (en utilisant par exemple des données récupérées via une API REST).
Vous pourrez superviser ce réseau à la voix ou via une interface tactile.

<img src="https://github.com/truillet/upssitech/blob/master/SRI/5A/ID/TP/images/rpi.jpg" align="center" width=300 alt="Raspberri Pi">


## Votre travail
1.  créez un client MQTT qui récupère les données de la météo locale via l’API OpenWeatherMap et les envoie sur le broker.
2.  créez  des  clients  MQTT  capables  d’envoyer  sur  le  broker  le  nombre  de  *VélÔToulouse* disponibles dans les stations les plus proches de l’UPSSITECH (en utilisant l'[API JCDecaux](https://developer.jcdecaux.com)) et de l’heure de passage des prochains bus à la station *Sports Universitaires* près du **U3** ([API Tisseo](https://data.toulouse-metropole.fr/explore/dataset/api-temps-reel-tisseo/api))
4. créez des clients MQTT à partir de micro-contrôleurs compatibles arduino et de capteurs de luminosité, température (ou autre) et envoyez les valeurs vers le broker MQTT.
5.  écrivez  un  client  tiers  capable  d’agréger  les  valeurs  des  différents  capteurs  positionnés  dans l’environnement (ex : toutes les températures d’une pièce) et de renvoyer périodiquement ces valeurs sur le broker (vous déterminerez les topics à utiliser).
6.  écrivez des agents permettant d'interagir à la voix (en entrée et en sortie) permettant de connaître la valeur d'un capteur.
7.  proposez enfin un dashboard de vos données en javascript, Python, … (et *MQTT* ou *MQTT over websoket*) permettant de suivre l’évolution des données dans le temps et déclencher des alertes à l’utilisateur.

### A votre disposition
* un broker MQTT (soit en ligne - mqtt.upssitech.fr, soit local - [Shiftr.io](https://www.shiftr.io))
* des arduino, NodeMCU, ESP32 ... et des capteurs
* des raspberry Pi 4 qui délivrent des vidéos sous forme de stream RTSP

### API REST intéressantes pour le projet
* **[API OpenWeatherMap](https://openweathermap.org/api)** : api météo
* **[API Tisseo](https://data.toulouse-metropole.fr/explore/dataset/api-temps-reel-tisseo/api)** : api tisseo
* **[API JCDecaux](https://developer.jcdecaux.com)** : api velô Toulouse

### API REST via des logiciels tiers
* [Murmure](https://www.murmure.app) : reconnaissance vocale en local (25 langues), api REST disponible
* [LMStudio}(https://lmstudio.ai/download) : faire tourner des LLM en local, api REST disponible
* [VoiceBox](https://github.com/jamiepine/voicebox) : voice cloning, api REST disponible

**Délai pour le rendu** : 16 décembre 2026
Le travail sera envoyé à Philippe.Truillet@upssitech.fr (Si vous avez des fichiers trop lourds à envoyer, vous pouvez utiliser un service cloud ou de transfert comme https://filesender.renater.fr)

