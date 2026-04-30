feuilles = [10, 9, 14, 18, 5, 4, 50, 3]
import math

def minimax(profondeur, index_noeud, est_max, valeurs):
    # Condition d'arrêt : on est au niveau des feuilles (profondeur 3)
    if profondeur == 3:
        return valeurs[index_noeud]

    if est_max:
        # On prend le maximum entre l'enfant gauche et l'enfant droit
        return max(minimax(profondeur + 1, index_noeud * 2, False, valeurs),
                   minimax(profondeur + 1, index_noeud * 2 + 1, False, valeurs))
    else:
        # On prend le minimum entre l'enfant gauche et l'enfant droit
        return min(minimax(profondeur + 1, index_noeud * 2, True, valeurs),
                   minimax(profondeur + 1, index_noeud * 2 + 1, True, valeurs))
# Test Minimax
res_minimax = minimax(0, 0, True, feuilles)
print("Résultat Minimax simple :", res_minimax)


def alpha_beta(profondeur, index_noeud, est_max, valeurs, alpha, beta):
    if profondeur == 3:
        return valeurs[index_noeud]
    if est_max:
        meilleur = -math.inf
        for i in range(2):
            val = alpha_beta(profondeur + 1, index_noeud * 2 + i, False, valeurs, alpha, beta)
            meilleur = max(meilleur, val)
            alpha = max(alpha, meilleur)
            
            # Condition d'élagage (La coupure)
            if beta <= alpha:
                break
        return meilleur
    else:
        meilleur = math.inf
        for i in range(2):
            val = alpha_beta(profondeur + 1, index_noeud * 2 + i, True, valeurs, alpha, beta)
            meilleur = min(meilleur, val)
            beta = min(beta, meilleur)
            # Condition d'élagage (La coupure)
            if beta <= alpha:
                break
        return meilleur
# Test Alpha-Beta
res_ab = alpha_beta(0, 0, True, feuilles, -math.inf, math.inf)
print("Résultat avec Alpha-Beta :", res_ab)

import math
# 1. Calcul de l'Entropie
def calculer_entropie(labels):
    total = len(labels)
    if total == 0: return 0
    
    # Compte combien de "Oui" et de "Non"
    counts = {}
    for l in labels:
        counts[l] = counts.get(l, 0) + 1
    entropie = 0
    for l in counts:
        p = counts[l] / total
        entropie -= p * math.log2(p)
    return entropie
# 2. Données d'exemple
# Chaque ligne : [Météo, Jouer]
# 0 = Pluie, 1 = Ensoleillé
data = [
    [1, "Oui"],
    [1, "Oui"],
    [0, "Non"],
    [0, "Non"]
]
# 3. Simulation de l'algorithme ID3
def simple_id3(dataset):
    labels = [row[1] for row in dataset]
    
    # Si tout est identique, on a fini !
    if len(set(labels)) == 1:
        return f"Feuille : {labels[0]}"
    
    # Sinon, on sépare par la météo (index 0)
    ensoleille = [row for row in dataset if row[0] == 1]
    pluie = [row for row in dataset if row[0] == 0]
    
    print(f"Entropie totale : {calculer_entropie(labels)}")
    print(f"Branche Ensoleillé : {simple_id3(ensoleille)}")
    print(f"Branche Pluie : {simple_id3(pluie)}")

# Lancement
simple_id3(data)

# Perceptron (algorithme d'apprentissage de perceptron),
import numpy as np

# 1. Données d'entraînement (Fonction AND)
# Entrées [x1, x2]
X = np.array([[0,0], [0,1], [1,0], [1,1]])
# Sorties attendues (y)
y = np.array([0, 0, 0, 1])
# 2. Initialisation
poids = np.zeros(2) # On commence avec des poids à 0
biais = 0
lr = 0.1  # Taux d'apprentissage (Learning Rate)
epochs = 10 # Nombre de passages sur les données
# 3. Boucle d'apprentissage
print("Début de l'apprentissage...")

for epoch in range(epochs):
    for i in range(len(X)):
        # Calcul de la prédiction (Somme pondérée)
        somme = np.dot(X[i], poids) + biais
        prediction = 1 if somme > 0 else 0
        
        # Calcul de l'erreur
        erreur = y[i] - prediction
        
        # Mise à jour des poids et du biais si erreur
        if erreur != 0:
            poids += lr * erreur * X[i]
            biais += lr * erreur

print("Apprentissage terminé.")
print(f"Poids finaux : {poids}")
print(f"Biais final : {biais}")

# 4. Test du modèle
print("\nTests :")
for x in X:
    res = 1 if (np.dot(x, poids) + biais) > 0 else 0
    print(f"Entrée {x} -> Prédiction: {res}")

