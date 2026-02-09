import random

def generer_tableau_aleatoire(taille_min, taille_max, val_min, val_max):
    taille = random.randint(taille_min, taille_max)
    return [random.randint(val_min, val_max) for _ in range(taille)]

# --- Stratégies de fusion ---

def fusion_simple(listes):
    resultat = []
    for l in listes:
        resultat += l
    return resultat

def fusion_triee(listes):
    return sorted(fusion_simple(listes))

def fusion_sans_doublons(listes):
    return list(set(fusion_simple(listes)))


def fusion_alternee(L1, L2):
    i, j = 0, 0
    res = []
    while i < len(L1) or j < len(L2):
        if i < len(L1):
            res.append(L1[i])
            i += 1
        if j < len(L2):
            res.append(L2[j])
            j += 1
    return res

def fusion_maintenant_ordre(L1, L2):
    # Suppose que L1 et L2 sont déjà triés
    i, j = 0, 0
    res = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1
    return res + L1[i:] + L2[j:]

# --- Données de test ---

# Tableau 1 : Création manuelle (trié pour tester la fusion e)
tableau_A = [10, 25, 30, 45]

# Tableau 2 : Génération aléatoire (Taille 3 à 6, Valeurs 0 à 50)
tableau_B = generer_tableau_aleatoire(3, 6, 0, 50)
# On le trie juste pour que la fusion "maintenant l'ordre" (e) soit cohérente
tableau_B.sort() 

print(f"Tableau A : {tableau_A}")
print(f"Tableau B : {tableau_B}")
print("-" * 30)

# --- Exécution des tests ---

# a. Fusion Simple
print(f"a. Fusion Simple : {fusion_simple([tableau_A, tableau_B])}")

# b. Fusion Triée
print(f"b. Fusion Triée : {fusion_triee([tableau_A, tableau_B])}")

# c. Fusion sans doublons
# Ajoutons un doublon forcé pour le test
test_doublons = [tableau_A, [10, 99]]
print(f"c. Sans Doublons (avec doublon 10 ajouté) : {fusion_sans_doublons(test_doublons)}")

# d. Fusion Alternée
print(f"d. Fusion Alternée : {fusion_alternee(tableau_A, tableau_B)}")

# e. Fusion maintenant l'ordre (Merge)
print(f"e. Fusion (ordre préservé) : {fusion_maintenant_ordre(tableau_A, tableau_B)}")