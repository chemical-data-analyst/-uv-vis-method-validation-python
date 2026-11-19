import numpy as np

# Ecart-type du signal blanc
sigma = 0.005

# Pente de la courbe d'etalonnage
S = 0.08

# Calcul du LOD et LOQ
LOD = (3.3 * sigma) / S
LOQ = (10 * sigma) / S

print("LOD :", LOD)
print("LOQ :", LOQ)