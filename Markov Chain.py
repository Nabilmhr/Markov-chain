import numpy as np
import random

p = random.random() # génère un nombre aléatoire entre 0 et 1 et l’assigne à la variable p

# Définition de la matrice de transition
P = np.array([[0, 0, 1, 0, 0],
[p, 0, (1-p), 0, 0],
[0, 0, p, 0, (1-p)],
[0, p, 0, (1-p), 0],
[0, 0, 0, 1, 0]])

# Nombre d’itérations
N = 1000000

# Etat initial
X = np.array([1, 0, 0, 0, 0])

# Simuler les états suivants
for i in range(N):
X = np.dot(X, P)

# Distribution invariante estimée
pi = X

# Afficher la distribution invariante estimée
print("Distribution invariante estimée : ", pi)
