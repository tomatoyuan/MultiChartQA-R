import matplotlib.pyplot as plt
import numpy as np

# Indicadores de salud
indicadores = ["HPV", "Marcadores tumorales", "Helicobacter pylori", "Exámenes clínicos (presión arterial, IMC, boca, oídos, nariz y garganta)", 
               "Exámenes funcionales (imagenología por rayos X, ecografía, electrocardiograma)", "Análisis bioquímicos y de laboratorio (análisis de sangre, orina, bioquímica,\n función hepática, función renal, función tiroidea, glucosa)"]
# Proporción correspondiente (%)
proporciones = [23.77, 30.67, 35.57, 44.83, 46.28, 61.89]

y = np.arange(len(indicadores))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar etiquetas de valores
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(indicadores)
ax.set_xlabel('Proporción (%)')
ax.set_title('Indicadores de salud más preocupantes para los consumidores de exámenes de salud en China en 2025')

plt.tight_layout()
plt.show()