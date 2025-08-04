import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e", "2025e", "2026e"]
# Tamaño actual del mercado de bebidas sin azúcar (en miles de millones de yuanes), datos consistentes con el gráfico
market_size = [32, 42, 67, 97, 118, 143, 168, 195, 231, 269, 301]
# Variación interanual (%), datos consistentes con el gráfico, agregar 0% para 2016 (sin datos de variación interanual)
yoy = [0, 28.8, 61.3, 43.7, 22.1, 21.4, 17.5, 16.2, 17.9, 16.7, 11.7]

# Crear un lienzo
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 600)

# Dibujar un gráfico de barras (tamaño del mercado, verde)
ax1.bar(years, market_size, color="#A4C639", label="Tamaño actual del mercado de bebidas sin azúcar (en miles de millones de yuanes)")
ax1.set_ylabel("Tamaño del mercado (en miles de millones de yuanes)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Crear un eje y secundario para dibujar un gráfico de línea (variación interanual, azul)
ax2 = ax1.twinx()

ax2.set_ylim(-120, 110)

ax2.plot(years, yoy, marker='o', color="#87CEEB", label="Variación interanual(%)", linewidth=2)
ax2.set_ylabel("Variación interanual(%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Agregar etiquetas de datos (tamaño del mercado)
for x, y in zip(np.arange(len(years)), market_size):
    ax1.text(x, y + 5, f'{y}', ha='center', va='bottom', color='black')

# Agregar etiquetas de datos (variación interanual)
for x, y in zip(np.arange(len(years)), yoy):
    ax2.text(x, y + 1, f'{y}%', ha='center', va='bottom', color='black')

# Agregar texto de descripción del CAGR
cagr_texts = [
    (0.2, 0.85, "CAGR = 36.1%"),
    (0.7, 0.85, "CAGR = 15.6%")
]
for x, y, text in cagr_texts:
    ax1.text(x, y, text, transform=ax1.transAxes, fontsize=12, ha='center', va='bottom')

# Establecer el título
ax1.set_title('Tamaño del mercado de bebidas sin azúcar en China desde 2016 hasta 2026', fontsize=14, fontweight='bold')

# Combinar leyendas
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Embelezar: Ocultar los bordes superior y derecho
for spine in ['top', 'right']:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()