# Markov-chain

Projet : Simulation de Chaîne de Markov pour la Disponibilité de Vélos

Ce projet a pour objectif d’analyser et de simuler une chaîne de Markov modélisant le nombre de vélos disponibles pour un individu, en considérant les probabilités de panne et de réparation.

Objectifs

Théorie des Chaînes de Markov : Montrer que  forme une chaîne de Markov, définir son espace d’états et calculer sa matrice de transition.

Distribution Invariante : Estimer la distribution invariante théorique et par simulation.

Probabilité Long Terme : Calculer la probabilité qu’aucun vélo ne soit disponible.

Données

Espace des états :

 : Aucun vélo disponible, le père travaille sur un vélo.

 : Un vélo fonctionne, aucun travail de réparation.

 : Un vélo fonctionne, le père travaille sur l’autre.

 : Deux vélos fonctionnent, aucun travail de réparation.

 : Deux vélos fonctionnent, le père travaille sur un.

Matrice de transition :

La matrice de transition est présentée comme suit :

Méthodologie

1. Simulation

Initialisation :

État initial : .

Probabilité  générée aléatoirement.

Itérations :

Appliquer la matrice de transition  pour simuler les états suivants.

Répéter  fois.

2. Estimation de la Distribution Invariante

Calculer la distribution invariante estimée après convergence.

3. Analyse

Comparer la distribution invariante estimée avec la distribution théorique.

Calculer la probabilité qu’aucun vélo ne soit disponible (état ).

