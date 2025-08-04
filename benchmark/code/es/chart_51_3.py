import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2023", "2024e", "2025e", "2026e", "2027e", "2028e"]
# Inversión en tecnología (en miles de millones de yuanes), aproximadamente simulada y se puede ajustar según la situación real
tech_investment = [517.6, 586.7, 672.9, 771.3, 881.5, 1020.1]
# Tasa de crecimiento (%), aproximadamente simulada y se puede ajustar según la situación real
growth_rate = [13.4, 14.7, 14.6, 14.3, 15.7, 16.8]

x = np.arange(len(years))  # Posiciones de las marcas en el eje x
bar_width = 0.5  # Ancho de las barras

fig, ax1 = plt.subplots(figsize=(14, 7))  # Aumentar aún más el ancho del gráfico

# Dibujar el gráfico de barras de la inversión en tecnología
bars = ax1.bar(x, tech_investment, width=bar_width, label='Inversión en Tecnología (Miles de Millones de Yuanes)', color='greenyellow')
ax1.set_ylabel('Inversión en Tecnología (Miles de Millones de Yuanes)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)

# Agregar etiquetas numéricas al gráfico de barras
for i, bar in enumerate(bars):
    height = bar.get_height()
    # Manejo especial para la última etiqueta
    if i == len(bars) - 1:
        ax1.annotate(f'{tech_investment[i]}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(15, 10),  # Desplazamiento hacia la parte superior derecha
                    textcoords="offset points",
                    ha='left', va='bottom',  # Alineación a la izquierda, abajo
                    fontsize=10)
    else:
        ax1.annotate(f'{tech_investment[i]}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 8),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

# Crear un segundo eje y y dibujar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
line, = ax2.plot(x, growth_rate, marker='o', markersize=7, label='Tasa de Crecimiento (%)', 
                color='dodgerblue', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento (%)', fontsize=12)

# Agregar etiquetas numéricas al gráfico de línea
for i, rate in enumerate(growth_rate):
    # Manejo especial para la última etiqueta
    if i == len(growth_rate) - 1:
        ax2.annotate(f'{rate}%',
                    xy=(x[i], rate),
                    xytext=(15, -15),  # Desplazamiento hacia la parte inferior derecha
                    textcoords="offset points",
                    ha='left', va='top',  # Alineación a la izquierda, arriba
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    else:
        ax2.annotate(f'{rate}%',
                    xy=(x[i], rate),
                    xytext=(-10, 10) if rate > 14.5 else (-10, -15),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

# Agregar un título
ax1.set_title('Inversión en Tecnología de la Industria de Seguros en China de 2023 a 2028', fontsize=14, pad=15)

# Combinar las leyendas
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=11)

# Embellir el gráfico
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Agregar líneas de cuadrícula horizontales
plt.tight_layout()  # Ajustar automáticamente el diseño

plt.show()