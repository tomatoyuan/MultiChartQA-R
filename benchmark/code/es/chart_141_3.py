import matplotlib.pyplot as plt
import numpy as np

# Datos
fuentes = ["Médicos", "Editores de medios profesionales de maternas e infantes", "Madres comunes del mismo círculo", "Amigos cercanos", "Marcas de productos pre - embarazo", "KOLs"]
porcentajes = [77.0, 61.1, 55.1, 44.2, 38.5, 20.4]

x = np.arange(len(fuentes))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange', label='Porcentaje de confianza (%)')
ax.set_ylabel('Porcentaje de confianza (%)')
ax.set_xlabel('Fuentes de información pre - embarazo')
ax.set_xticks(x)
ax.set_xticklabels(fuentes, rotation=15, ha='right')
ax.set_title('Fuentes de información pre - embarazo en las que confía la población china en etapa de pre - embarazo en 2023')

# Agregar etiquetas numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()