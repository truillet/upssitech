# Bureau d’Etudes - un superviseur de capteurs réels et virtuels
*par groupe de 5 à 8)*

Il s’agit de créer, de gérer et de superviser un réseau de capteurs à partir de données *réelles locales* (température, pression, luminosité, taux d’humidité, détection, ...)
et à distance (en utilisant par exemple des données récupérées via une API REST).

Pour ce faire :
1.  créez un client MQTT qui récupère les données de la météo locale via l’API OpenWeatherMap et les envoie sur le broker.
2.  créez  des  clients  MQTT  capables  d’envoyer  sur  le  broker  le  nombre  de  *VélÔToulouse* disponibles dans les stations les plus proches de l’UPSSITECH (en utilisant l'[API JCDecaux](https://developer.jcdecaux.com)) et de l’heure de
passage des prochains bus à la station *Sports Universitaires* près du **U3** ([API Tisseo](https://data.toulouse-metropole.fr/explore/dataset/api-temps-reel-tisseo/api)
4. créez des clients MQTT à partir de micro-contrôleurs compatibles arduino (ESP) et de capteurs de luminosité, température (ou autre) et envoyez les valeurs vers le broker MQTT.
5.  écrivez  un  client  tiers  capable  d’agréger  les  valeurs  des  différents  capteurs  positionnés  dans l’environnement (ex : toutes les températures d’une pièce) et de renvoyer périodiquement ces
valeurs sur le broker (vous déterminerez les topics à utiliser).
6.  proposez enfin un dashboard de vos données en javascript, Python, … (et *MQTT* ou *MQTT over websoket*) permettant de suivre l’évolution des données dans le temps et déclencher des alertes
à l’utilisateur.

## A votre disposition

* un broker MQTT en ligne
* 

## Exemples d’API REST intéressantes
* **OpenWeatherMap**, https://openweathermap.org/api
* **Tisseo**, https://data.toulouse-metropole.fr/explore/dataset/api-temps-reel-tisseo/api
* **JCDecaux**, https://developer.jcdecaux.com


