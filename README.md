# Projet Eliza

Le projet Eliza était un projet d'une durée de 3 semaines dans lequel nous devions concevoir un ChatBot répondant à une problématique, une cible précis. Il fallait aborder tout la partie buisness du ChatBot, mais aussi les questions éthique et avoir une bonne promotion de notre produit final.

## Documentation 

Pour mener à bien ce projet, il nous a fallu examiner le marché, trouver des pistes sur lesquelles avancées pour nous permettre d'avoir une marche de progression intéressante. Nous avons donc détaillé nos envies et nos but pour ce projet. Nous avons pu le faire par un benchmark regroupant nos objectifs, nos concurrents, nos cibles et nos besoins, aisni qu'une analyse SWOT et les fonctionnalité pour notre succès.

Par la suite, il nous a fallu comprendre l'enjeux et l'impact que pouvait avoir notre buissness. En effet, nos objectifs maintenant clairement exposer, il nous fallait savoir comment structurer notre projet, les coûts que celui-ci pourrait avoir, l'efficacité et l'optimisation de celui-ci. Mais aussi le retour sur investissement et plus généralement les sources de revenues que nous aurions pu avoir grâce à celui-ci. Nous avions aussi des ambitions, ils nous fallait tout au long de la conception de notre produit, na pas manquer les opportunité ainsi que les futurs occasion de pouvoir se developper.

Et enfin, car cet élément est au coeur de nombreux débats et est une vraie difficulté de notre époque. La question des données personnelles en ligne et du respect de la vie privée. 
Il a fallu nous assurer que les règles de la RGPD était respectées par notre produit. Trouver ses points faibles et les résoudre, et comprendre les enjeux de tous cela. 

## Bot

Notre ChatBot, VetBot, est spécialiste des animaux, plutôt tourné du côté vétérinaire. Fine-tuner depuis un modèle open-source mistral proposé par le site Ollama, il a été modifié, amélioré et pensé pour répondre correctement à notre sujet. 
Celui-ci est capable de répondre de manière naturelle à l'utilisateur.
Celui-ci possède une mémoire qui lui permet de tenir une vrai conversation, un véritable échange avec l'utilisateur.

Le bot possède plusieurs features principales. 

- /help : Cette commande permet tout simplement d'apporter de l'aide à l'utilisateur pour comprendre comment utiliser notre bot.

- /delete : Cela permet de supprimer n-messages du channel permettant d'effacer partiellement une conversation.

- /infos : Cette fonctionnalité permet au curieux, d'en apprendre plus sur un animal, une race ou une espèce. Elle permet de partager : la taille, le poids et une description du sujet rechercher

- /diagnostic : Enfin, cette commande permet à l'IA de faire un diagnostic de la situation que vous lui partager. Elle se verra rassurante et pourra selon si elle semble voir un danger pour votre animal vous suggerer plus ou moins fortement d'aller voir un vétérinaire au plus vite, pour la santé de votre animal.

Il faut tout de même noté que VetBot n'est pas vétérinaire. il ne fera jamais de dignostique détaillé, il ne pourra rien prescrire. Il n'est là qu'à titre d'information, d'aide mais il ne doit être en aucun cas votre solution miracle.


## Landing Page

Pour promouvoir notre ChatBot, nous avons créer une landing page présentant ses différentes fonctionnalités. On y présente notre bot, son but, son rôle, ses compétences et propose à l'utilisateur de l'ajouter à son serveur Discord. Le style de cette page rappelle l'univers animalier et vétérinaire avec le vert et les animaux présent. L'interface et l'expérience utilisateur à été le moteur clé de ce projet, c'est pourquoi cette page propose un visuel agréable et professionnelle.


## Utilisation de notre projet

Pour pouvoir profiter de notre projet rien de plus simple, il vous suffit de suivre ces étapes : 

Après avoir installer tout le projet, lancer un terminal. <br>
Se mettre au niveau de la racine du projet et faire ces commandes : <br>

```
- cd anticipay-bot
- npm install
- npm run dev
``` 

Après avoir fais tout cela, vous devriez avoir dans le terminal un ligne écrit : 
```
Local:   http://localhost:5173/
```
Vous faire ctrl + click sur le lien ce qui devrai vous envoyer sur internet avec cette même URL (http://localhost:5173/)<br>
Sinon la rentrer simplement dans votre navigateur internet.

Une fois sur la page, vous devriez trouver un bouton vert avec écrit "Ajouter à Discord". <br>
Cliquez dessus et faite la démarche pour l'ajouter à votre serveur avec des droits lui permettant d'écrire, de supprimer des messages et de faire des intégrations pour vous permettre d'accéder à toutes ses fonctionnalitées.

Une fois ajouté à votre serveur, il ne vous suffit plus que d'utiliser ses différentes features pour obtenir l'aide nécessaire au bien-être de votre/vos anim(al/aux). N'hésitez pas à commencer par faire /help pour avoir toutes les informations sur ses fonctionnalitées !