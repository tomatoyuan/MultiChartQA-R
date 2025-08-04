import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
meses = ["Ene", "Feb", "Mar"]
años = ["2023", "2024", "2025"]
datos = [
    [67.3, 64.1, 62.9],
    [67.2, 64.9, 63.3],
    [69.7, 66.9, 63.4]
]
tazas_de_crecimiento = ["Año sobre año -1.9%", "Año sobre año -2.5%", "Año sobre año -5.1%"]
colores = ["#a5d65d", "#81c784", "#4bb7e6"]  # Coincidir con los colores del gráfico

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras agrupadas
x = np.arange(len(meses))
ancho_de_barra = 0.25
for i in range(3):
    ax.bar(x + i * ancho_de_barra, datos[i], width=ancho_de_barra, color=colores[i], label=años[i], edgecolor='white')
    # Agregar etiquetas de datos
    for j, val in enumerate(datos[i]):
        ax.text(x[j] + i * ancho_de_barra, val - 3, f'{val}', ha='center', va='bottom', fontsize=9)

# Agregar anotaciones año sobre año
for i in range(3):
    ax.text(x[i] + 1 * ancho_de_barra, max(datos[i]) + 2, tazas_de_crecimiento[i], ha='center', va='bottom', fontsize=10, color='blue')

# Emprolijar la configuración
ax.set_title("mUserTracker-2023-2025Q1\nTiempos de uso diario de dispositivos únicos", fontsize=12, fontweight='bold')
ax.set_xticks(x + ancho_de_barra)
ax.set_xticklabels(meses)
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()