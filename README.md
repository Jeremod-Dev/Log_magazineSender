# LOG_SENDER GENERATEUR
Logiciel de modification de Template simple pour communiquer par courriel avec les lecteurs du Log_Magazine

## Qu'est ce que le Log_Magazine ?

Le Log_Magazine est un journal/magazine produit par des étudiants volontaires du département Informatique de l'Institut Universitaire de Technologie du Limousin. Ce magazine est dû a l'initiative de la professeure de communication du département. Par la suite, les étudiants volontaires ont étoffé l'idée. Ce mensuel admet à chaque fois un nouveau thème, sur lequel se base les articles. Finalement, tous les premiers du mois (hors Aout et Septembre) la rédaction publie le magazine.

![Couverture du Log_Magazine de Mai 2021](https://github.com/Jeremod-Dev/Log_magazineSender/blob/main/image/Couverture.PNG)

*Couverture du Log_Magazine de Mai 2021* 

## Contexte du projet

Pour proposer à tous les étudiants et enseignants du département le numéro du mois, l'éditrice du Log_Magazine, envoie un courriel sur une liste de diffusion, avec un lien vers le site du Log_Magazine et le magazine au format PDF. En vue d'améliorer la communication externe du Log, certains membres de la rédaction, ont émis l'hypothèse d'insérer du XHTML dans le courriel afin d'obtenir un visuel plus attrayant.

![Tempalte exemple de courriel de communication](https://github.com/Jeremod-Dev/Log_magazineSender/blob/main/image/Template.PNG)

Seulement, pour faire ce rendu, il faut mettre la main dans code, hors cela peut-être plutôt fastidieux pour un non-développeur, surtout s'il y a plusieurs templates differents. Pour rendre plus accessible la creation d'un courriel, j'ai développé à mon initiative une application de bureau permettant de générer des courriels facilement.

## Comment utiliser le logiciel ?

- Etape 1: Ce connecter via un des mots de passe. Le logiciel étant au service du Log_Magazine, j'ai préféré limiter l'accès.

![Page d'accueil du logiciel](https://github.com/Jeremod-Dev/Log_magazineSender/blob/main/image/HomePage.PNG)

- Etape 2: Selectionner votre template. *Pour que votre template soit valide, il doit respecter les conditions cité plus bas dans le readme*

- Etape 3: Saisissez le lien vers le PDF.

- Etape 4: Saisissez le texte 

- Etape 5: Prévisualisez votre courriel.

![Page de création de courriel du logiciel](https://github.com/Jeremod-Dev/Log_magazineSender/blob/main/image/CreationPage.PNG)

Dans cette première version, vous ne pouvez que récuperer dans votre presse papier le code source pour l'insérer par vous même dans un mail. Cette tache est plutôt difficile à effectuer, par conséquent la prochaine version du logiciel incluera l'envoi de courriel.

**Lors de l'utilisation de l'application veuillez NE JAMAIS renommer, déplacer ou modifier le fichier `4050af11e3cede12a7c250b5f50fcd1c.html`. Dans le cas contraire, le logiciel admettera un disfonctionnement.**

## Comment générer un template valide ?

### Conditions générales:

Vous devez générer un template qui a pour objectif d'être envoyé par courriel, dans ce cas vous devez prendre en compte que les boites mail ne gerent pas toutes les technologies [(Technologies supportées)](https://www.campaignmonitor.com/css/) :

- Les langage XHTML + CSS  *ne pas en abuser*
- Les images doivent être stocké dans un endroit accessible sur internet. Votre template lui fera référence.

Pour vous aider dans le developpement de votre template, je renvois vers le tutoriel de [Grafikart.fr](https://www.youtube.com/watch?v=xeNjM3miO7k). Pour créer un bouton cliquable vous pouvez utiliser ce [générateur](https://buttons.cm/).

### Conditions liées aux générateurs:

Le logiciel concidère que votre template est valide. Pour que votre template fonctionne correctement avec le logiciel vous devez respecter plusieurs conditions **obligatoire**:

- Un bouton vers le PDF. Pour le lien mettez `{}`.
- Un champ de texte. Ce champ sera balisé avec `<pre>{}</pre>`. Veuillez faire attention que les accolades soient tangentes avec la balise ouvrante.
- Le **bouton** doit être placé avant **la zone de texte**.
- Le template ne doit pas contenir de caractères spéciaux, ni d'accolades que ce soit dans **le code** et dans **les commentaires**.

![Exemple bouton](https://github.com/Jeremod-Dev/Log_magazineSender/blob/main/image/img1.PNG)

*exemple pour le bouton*

![Exemple bouton](https://github.com/Jeremod-Dev/Log_magazineSender/blob/main/image/img2.PNG)

*exemple pour le texte*