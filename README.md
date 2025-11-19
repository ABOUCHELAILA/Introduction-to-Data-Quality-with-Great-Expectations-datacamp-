# Introduction-to-Data-Quality-with-Great-Expectations-datacamp-
**Why is data quality important?**

Why is data quality important? Well, if we put garbage into a model, then we'll get garbage out. No matter how advanced or well-trained a model is, if the quality of the input data is poor, then the quality of the model will ultimately be poor, too. A model can only be as good as the data going in! That's why data quality is so important -- it affects everything downstream of it.

**Qu’est-ce que Great Expectations ?**

Great Expectations (GX) est une plateforme pour gérer la qualité des données.

Son objectif principal : décrire les données avec des tests explicites (appelés Expectations) et vérifier automatiquement si les données respectent ces tests.

Deux façons d’utiliser GX

GX Cloud

Interface web, facile à utiliser pour visualiser et gérer les validations de données.

Permet de suivre la qualité des données dans un projet de manière collaborative.

GX Core

Package Python utilisé dans ce cours.

Intégré dans Python, il permet de tirer parti de la puissance et de la flexibilité du langage pour :

Créer des Expectations

Valider des données

Générer des rapports et Data Docs

Idéal pour automatiser la qualité des données dans des pipelines ou analyses Python.
**Qu’est-ce qu’un Data Context ?**

Avant de définir des Expectations (règles de qualité des données), il faut créer un Data Context.

C’est le point d’entrée principal pour utiliser Great Expectations, un peu comme un contexte SQL pour gérer et exécuter des requêtes.
Rôle du Data Context

Fournir une API pour le projet GX

Permet d’accéder et de mettre à jour tous les éléments du projet Great Expectations.

Définir le stockage des métadonnées

Où sont stockés les composants essentiels :

Data Sources : les sources de données que tu veux valider

Expectation Suites : les ensembles de règles de qualité (Expectations)

Checkpoints : points de contrôle pour exécuter les validations

Data Docs : documentation et rapports de validation

Gérer les sorties et métriques

Contient les Validation Results (résultats de la vérification) et les métriques associées pour analyser la qualité des données.

Résumé simple

Le Data Context est la base de tout projet GX.

Il permet de connecter Great Expectations à tes données, de définir des règles de qualité, et de gérer les résultats.

Créer un Data Context est donc la première étape avant de définir des Expectations.
Pour t’entraîner à Great Expectations (GX) :

Tu installes et utilises GX Core, la version open source en Python.

Avec GX Core, tu peux :

Créer un Data Context

Définir des Expectation Suites

Exécuter des validations sur tes données

Générer des Data Docs (rapports HTML que tu peux ouvrir dans ton navigateur)

Tout cela se fait localement ou sur ton serveur, donc pas besoin de GX Cloud pour apprendre ou pratiquer.

💡 Astuce : Commence avec GX Core pour te familiariser avec les concepts, puis si tu veux collaborer avec d’autres ou avoir un dashboard complet, tu pourras passer à GX Cloud plus tard.
