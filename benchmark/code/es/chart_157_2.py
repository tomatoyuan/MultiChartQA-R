import matplotlib.pyplot as plt
import numpy as np

# Datos
años = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023])
tamaño_del_mercado = [1195, 1261, 1258, 1202, 1337, 1472, 1570]
tasa_de_crecimiento = [None, 5.52, -0.24, -4.45, 11.23, 10.10, 6.66]

# Crear la figura
fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de barras
bar = ax1.bar(años, tamaño_del_mercado, color='#38C6D9', width=0.6, label='Tamaño del mercado')
ax1.set_ylabel('Tamaño del mercado (miles de millones de yuanes)', fontsize=12)
ax1.set_ylim(0, 2000)

# Etiquetar los valores
for i, val in enumerate(tamaño_del_mercado):
    ax1.text(años[i], val + 30, str(val), ha='center', fontsize=10)

# Gráfico de línea
ax2 = ax1.twinx()
ax2.plot(años[1:], tasa_de_crecimiento[1:], color='darkred', linestyle='--', marker='o', linewidth=2, label='Tasa de crecimiento')
for i, val in enumerate(tasa_de_crecimiento[1:], 1):
    ax2.text(años[i], tasa_de_crecimiento[i] + 0.8, f'{val:.2f}%', color='darkred', fontsize=10, ha='center')

ax2.set_ylabel('Tasa de crecimiento', fontsize=12)
ax2.set_ylim(-10, 15)

# Título y leyenda
plt.title('Evolución del tamaño del mercado de proteínas alternativas en China entre 2017 y 2023', fontsize=16, weight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.show()