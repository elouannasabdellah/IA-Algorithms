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