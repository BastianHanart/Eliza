# Cadre Légal et Conformité RGPD : Chatbot de Prévention & Budget Santé Animale

## Introduction
Le document définit les piliers juridiques et les obligations de conformité pour le déploiement du Chatbot.

---

## 1. Cadre Médical

### 1.1. Interdiction de l'Exercice Illégal de la Médecine Vétérinaire
**Conformément au Code de la santé publique et au Code rural et de la pêche maritime (Art. L243-1), seul un vétérinaire inscrit à l'Ordre peut établir un diagnostic, prescrire un traitement ou réaliser une chirurgie.**
* **Obligation du Chatbot :** Le système doit être présenté explicitement comme un outil d'aide de conseil en prévention

* **Clause de Non-Responsabilité :** Nous ne nous engageons pas des décisions prises après avoir consulté notre chatbot

### 1.2. Détection d'urgence et action
* **Indice d'Urgence :** Le chatbot doit intégrer un algorithme de détection de mots-clés critiques (ex: "hémorragie", "convulsions", "ingestion toxique"). 
* **Action :** En présence de ces mots, le chatbot doit interrompre le message en cours pour afficher les coordonnées des urgences vétérinaires les plus proches.

---

## 2. Protection des Données Personnelles (RGPD)

Bien que les données concernent principalement des animaux, elles sont juridiquement rattachées au propriétaire et constituent donc des **données à caractère personnel**.

### 2.1. Nature des Données Collectées
* **Données utilisateur :** Nom, prénom, adresse email, code postal.
* **Données de l'Animal :** Espèce, race, âge, antécédents médicaux déclarés.
* **Données Financières :** type d'assurance souscrite.

### 2.2. Cadre légale
1.  **Consentement (Art. 6.1.a RGPD) :** Recueilli via une case à cocher non pré-cochée lors de l'inscription.
2.  **Exécution du contrat (Art. 6.1.b RGPD) :** Nécessaire pour fournir les calculs budgétaires personnalisés.

### 2.3. Droits des Utilisateurs
Le chatbot doit permettre aux utilisateurs d'exercer leurs droits simplement :
* **Droit d'accès et de rectification :** Possibilité de modifier leur profil ou celui de l'animal.
* **Droit à l'oubli :** Suppression du compte et de l'historique des conversations sous 30 jours.

### 2.4. Durée de Conservation
* **Comptes actifs :** Toute la durée de vie de l'animal plus 2 ans après la dernière activité.
* **Comptes inactifs :** Suppression ou anonymisation après 3 ans d'inactivité.

---

## 3. Transparence et Information Commerciale

### 3.1. Variabilité des Tarifs
Le chatbot doit préciser que les estimations financières sont basées sur des moyennes régionales et n'engagent pas les cliniques tierces. 
* **Statistique de référence :** En France, les tarifs vétérinaires peuvent varier de **20% à 50%** entre une zone rurale et une zone urbaine.

---

## 4. Sécurité des Données

* **Hébergement :** Les données doivent être hébergées sur des serveurs situés au sein de l'Union Européenne.
* **Chiffrement :** Utilisation d'outils pour la protection des données.
* **Anonymisation :** Pour l'entraînement de l'IA, les données doivent être strictement anonymisées.

---

## 5. Responsabilité Civile

Le chatbot peut être tenu responsable en cas de :
1.  **Perte de chance :** Si le chatbot rassure à tort un propriétaire alors que l'animal est en détresse vitale. (d'où la mise en place d'une détection de mot d'urgence).
