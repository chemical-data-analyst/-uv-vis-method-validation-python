import numpy as np

# Mesures repetees de la meme solution
mesures = [0.598, 0.602, 0.601, 0.599, 0.600]

# Calculer la moyenne
moyenne = np.mean(mesures)

# Calculer l'ecart-type
ecart_type = np.std(mesures, ddof=1)

# Calculer le coefficient de variation
cv = (ecart_type / moyenne) * 100

print("Moyenne :", moyenne)
print("Ecart-type :", ecart_type)
print("Coefficient de variation :", cv, "%")