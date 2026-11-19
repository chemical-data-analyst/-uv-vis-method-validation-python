import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lire les donnees
data = pd.read_csv("donnees_uv_vis.csv")

# Extraire les variables
concentration = data["Concentration"]
absorbance = data["Absorbance"]

# Regression lineaire
pente, ordonnee = np.polyfit(concentration, absorbance, 1)

# Calculer les valeurs predites
absorbance_predite = pente * concentration + ordonnee

# Calculer R2
r2 = np.corrcoef(absorbance, absorbance_predite)[0, 1] ** 2

# Afficher les resultats
print("Pente :", pente)
print("Ordonnee a l'origine :", ordonnee)
print("Coefficient R2 :", r2)

# Tracer la courbe
plt.scatter(concentration, absorbance, label="Mesures")
plt.plot(concentration, absorbance_predite, color="red", label="Regression lineaire")

plt.xlabel("Concentration")
plt.ylabel("Absorbance")
plt.title("Courbe d'etalonnage UV-Vis")
plt.legend()
plt.grid()

plt.savefig("courbe_etalonnage.png")
plt.show()