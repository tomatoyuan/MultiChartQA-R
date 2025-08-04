import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ['2022', '2023']
salud_medica = [4.08, 4.64]
suplementos = [67.09, 70.83]
tradicionales = [28.83, 24.53]

ancho_barra = 0.5
x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar el gráfico de barras apiladas
p1 = ax.bar(x, tradicionales, ancho_barra, label='Productos nutricionales de tonificación tradicional', color='#b2df8a')
p2 = ax.bar(x, suplementos, ancho_barra, bottom=tradicionales, label='Suplementos dietéticos y productos de salud', color='#fdbf6f')
base2 = [tradicionales[i] + suplementos[i] for i in range(len(x))]
p3 = ax.bar(x, salud_medica, ancho_barra, bottom=base2, label='Salud médica', color='#1f78b4')

# Agregar etiquetas de texto
for i in range(len(x)):
    ax.text(x[i], tradicionales[i] / 2, f'{tradicionales[i]:.2f}%', ha='center', va='center', fontsize=10)
    ax.text(x[i], tradicionales[i] + suplementos[i] / 2, f'{suplementos[i]:.2f}%', ha='center', va='center', fontsize=10)
    ax.text(x[i], base2[i] + salud_medica[i] / 2, f'{salud_medica[i]:.2f}%', ha='center', va='center', fontsize=10)

# Configurar etiquetas y título
ax.set_xticks(x)
ax.set_xticklabels(años, fontsize=12)
ax.set_ylabel('Proporción de ventas (%)')
ax.set_title('Proporción de ventas de diferentes categorías en los \ne - comercios de Douyin y Kuaishou entre 2022 y 2023', fontsize=14, weight='bold')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=10, frameon=False)

# Aclaración de la fuente de datos
plt.figtext(0.5, -0.05, 'Fuente de datos: Feigua Data (feigua.cn), Plataforma de estadísticas: Douyin, Kuaishou, Período de datos: 2022.01 - 2024.03',
            wrap=True, horizontalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()