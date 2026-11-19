import pandas as pd
import numpy as np

np.random.seed(42)

concentrations = [2, 4, 6, 8, 10]

absorbances = []

for concentration in concentrations:
    absorbance = 0.05 + 0.08 * concentration
    absorbance += np.random.normal(0, 0.01)
    absorbances.append(absorbance)

data = pd.DataFrame({
    "Concentration": concentrations,
    "Absorbance": absorbances
})

data.to_csv("donnees_uv_vis.csv", index=False)

print(data)