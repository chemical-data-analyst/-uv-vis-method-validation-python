import pandas as pd
import numpy as np

# Lire les donnees
data = pd.read_csv("donnees_uv_vis.csv")

concentration = data["Concentration"]
absorbance = data["Absorbance"]

# Calculer la droite d'etalonnage
pente, ordonnee = np.polyfit(concentration, absorbance, 1)

# Absorbance de l'echantillon inconnu
absorbance_inconnue = 0.60

# Calculer la concentration
concentration_inconnue = (absorbance_inconnue - ordonnee) / pente

print("Absorbance inconnue :", absorbance_inconnue)
print("Concentration calculee :", concentration_inconnue)