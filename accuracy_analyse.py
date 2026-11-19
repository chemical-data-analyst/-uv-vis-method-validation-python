import numpy as np

# Valeur de reference
valeur_reference = 10.0

# Resultats experimentaux
resultats = [9.8, 9.9, 10.1, 10.0, 9.9]

# Calculer la moyenne
moyenne = np.mean(resultats)

# Calculer le taux de recuperation
recuperation = (moyenne / valeur_reference) * 100

# Calculer l'erreur relative
erreur = abs(moyenne - valeur_reference) / valeur_reference * 100

print("Moyenne :", moyenne)
print("Taux de recuperation :", recuperation, "%")
print("Erreur relative :", erreur, "%")