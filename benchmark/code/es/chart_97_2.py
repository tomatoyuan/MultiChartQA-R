import matplotlib.pyplot as plt
import numpy as np

# Datos de la situación de edad
categorias_edad = ["Menos de 24", "25 - 34", "35 - 44", "45 y mayores"]
porcentajes_edad = [29.3, 41.5, 21.6, 7.6]
# Datos de la situación matrimonial
categorias_matrimonio = ["Soltero", "Casado con hijos", "Casado sin hijos"]
porcentajes_matrimonio = [60.7, 34.1, 5.2]
# Esquema de colores libre (ajustable)
color_barra = "#A4C639"  # Color del gráfico de barras
colores_torta = ["#A4C639", "#87CEEB", "#FFD700"]  # Colores del gráfico de torta

# Crear un lienzo con dos columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Dibujar un gráfico de barras horizontales para la situación de edad
y = np.arange(len(categorias_edad))
ax1.barh(y, porcentajes_edad, color=color_barra, height=0.6)
ax1.set_yticks(y)
ax1.set_yticklabels(categorias_edad)
ax1.set_title("Situación de edad de los aficionados al fútbol chino en 2022", fontsize=12, fontweight="bold")
# Agregar anotaciones de edad
for i, val in enumerate(porcentajes_edad):
    ax1.annotate(f'{val}%', (val + 1, i), va='center', fontsize=9)

# Dibujar un gráfico de torta para la situación matrimonial
wedges, texts, autotexts = ax2.pie(
    porcentajes_matrimonio,
    labels=categorias_matrimonio,
    colors=colores_torta,
    autopct='%1.1f%%',
    startangle=90
)
ax2.set_title("Situación matrimonial de los \naficionados al fútbol chino en 2022", fontsize=12, fontweight="bold")
# Embelezar las anotaciones del gráfico de torta (color, tamaño)
for text, autotext in zip(texts, autotexts):
    text.set_color('black')
    autotext.set_color('black')
    autotext.set_fontsize(9)

# Embelecimiento: Ocultar bordes
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()