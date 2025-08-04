import matplotlib.pyplot as plt
import numpy as np

# Organización de datos
empresas = ["Grupo Yili", "Bright Dairy", "New Hope Dairy"]
# Ingresos operativos en 2022 (miles de millones de yuanes)
ingresos_2022 = [1227.0, 282.15, 100.06]
# Ingresos operativos en el primer semestre de 2023 (miles de millones de yuanes)
ingresos_2023h = [659.82, 141.39, 52.98]
# Proporción de leche líquida en 2022 (%)
proporcion_2022 = [69.22, 57.03, 87.76]
# Proporción de leche líquida en 2023 (%)
proporcion_2023 = [64.29, 58.40, 90.94]

x = np.arange(len(empresas))  # Nombres de las empresas lácteas como coordenadas en el eje X
ancho = 0.35  # Ancho de las barras

# Crear un lienzo
fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras de los ingresos operativos en 2022 y el primer semestre de 2023
bar_2022 = ax1.bar(x - ancho/2, ingresos_2022, ancho, label='Ingresos operativos en 2022', color='#FF7F50')
bar_2023h = ax1.bar(x + ancho/2, ingresos_2023h, ancho, label='Ingresos operativos en el primer semestre de 2023', color='#40E0D0')

# Etiquetar los valores de los ingresos operativos
for bar in bar_2022 + bar_2023h:
    altura = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, altura + 5, f'{altura:.1f} miles de millones de yuanes', ha='center', va='bottom')

# Configurar el eje Y izquierdo (ingresos operativos)
ax1.set_ylabel('Ingresos operativos (miles de millones de yuanes)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(empresas, fontsize=12)
ax1.legend(loc='lower left')

# Crear el eje Y derecho (proporción de leche líquida)
ax2 = ax1.twinx()
ax2.plot(x, proporcion_2022, marker='o', color='#FFD700', label='Proporción de ingresos de leche líquida en 2022', linewidth=2)
ax2.plot(x, proporcion_2023, marker='s', color='#DA70D6', label='Proporción de ingresos de leche líquida en 2023', linewidth=2)

# Etiquetar los valores de la proporción de leche líquida
for i, (p22, p23) in enumerate(zip(proporcion_2022, proporcion_2023)):
    ax2.text(i, p22 + 1, f'{p22:.2f}%', ha='center', va='bottom', color='#FFD700')
    ax2.text(i, p23 + 1, f'{p23:.2f}%', ha='center', va='bottom', color='#DA70D6')

# Configurar el eje Y derecho (proporción de leche líquida)
ax2.set_ylabel('Proporción de ingresos de leche líquida (%)', fontsize=12)
ax2.legend(loc='center right')

# Título del gráfico
plt.title('Ingresos operativos y proporción de ingresos de leche líquida de algunas empresas lácteas chinas', fontsize=14, pad=20)
plt.tight_layout()
plt.show()