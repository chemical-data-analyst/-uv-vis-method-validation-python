import pandas as pd
import numpy as np
from openpyxl.drawing.image import Image
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart,Reference

# Lire les donnees
data = pd.read_csv("donnees_uv_vis.csv")

# Calculer la regression lineaire
concentration = data["Concentration"]
absorbance = data["Absorbance"]

pente, ordonnee = np.polyfit(concentration, absorbance, 1)

absorbance_predite = pente * concentration + ordonnee
r2 = np.corrcoef(absorbance, absorbance_predite)[0, 1] ** 2

# Creer le rapport Excel
wb = Workbook()
ws = wb.active
ws.title = "Rapport UV-Vis"

# Titre
ws["A1"] = "Validation de la methode analytique UV-Vis"
ws["A1"].font = Font(bold=True, size=14)

# Resultats
resultats = [
    ["Indicateur", "Resultat"],
    ["Pente", pente],
    ["Ordonnee a l'origine", ordonnee],
    ["Coefficient R2", r2],
    ["LOD", 0.20625],
    ["LOQ", 0.625],
    ["Recovery (%)", 99.4],
    ["CV (%)", 0.2635]
]

for ligne in resultats:
    ws.append(ligne)

# Mise en forme
for cell in ws[2]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="4472C4")

for colonne in ws.columns:
    ws.column_dimensions[colonne[0].column_letter].width = 28

# Alignement
for ligne in ws.iter_rows():
    for cell in ligne:
        cell.alignment = Alignment(horizontal="center")
# Ajouter la courbe d'etalonnage
img = Image("courbe_etalonnage.png")
img.width = 600
img.height = 350
ws.add_image(img, "D2")
# Tableau des indicateurs de validation
ws["A12"] = "Indicateur"
ws["B12"] = "Valeur (%)"

ws["A13"] = "Recovery"
ws["B13"] = 99.4

ws["A14"] = "CV"
ws["B14"] = 0.2635

ws["A15"] = "Erreur relative"
ws["B15"] = 0.6

# Creer le graphique
chart = BarChart()
chart.title = "Indicateurs de validation"
chart.y_axis.title = "Pourcentage (%)"
chart.x_axis.title = "Indicateurs"

data_chart = Reference(ws, min_col=2, min_row=12, max_row=15)
categories = Reference(ws, min_col=1, min_row=13, max_row=15)

chart.add_data(data_chart, titles_from_data=True)
chart.set_categories(categories)

chart.height = 8
chart.width = 14

ws.add_chart(chart, "D22")
# Sauvegarder
wb.save("rapport_uv_vis.xlsx")

print("Rapport Excel cree avec succes !")