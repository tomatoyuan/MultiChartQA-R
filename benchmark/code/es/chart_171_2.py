import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Datos
meses = ['Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
datos_2022 = [87, 100, 96, 88, 92, 91, 98]  # Valores estructurados
crecimiento = [0.13, 0.0, 0.04, 0.32, 0.30, 0.26, 0.02]
datos_2023 = [datos_2022[i] * (1 + crecimiento[i]) for i in range(len(datos_2022))]

x = np.arange(len(meses))
ancho = 0.35

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras
barras_2022 = ax.bar(x - ancho/2, datos_2022, ancho, label='2º semestre 2022', color='#e55322')
barras_2023 = ax.bar(x + ancho/2, datos_2023, ancho, label='2º semestre 2023', color='black')

# Agregar etiquetas de valores (2022 y 2023)
for i in range(len(x)):
    # Barras de 2022 - Etiqueta interna
    ax.text(x[i] - ancho/2, datos_2022[i] - 3,
            f'{int(datos_2022[i])}', ha='center', va='top', fontsize=10, color='white')

    # Barras de 2023 - Etiqueta externa en la parte superior
    ax.text(x[i] + ancho/2, datos_2023[i] + 4,
            f'{int(datos_2023[i])}', ha='center', va='bottom', fontsize=10, color='black')

# Agregar anotaciones de tasa de crecimiento (ligeramente desplazadas hacia arriba)
for i, (x_pos, val) in enumerate(zip(x, datos_2023)):
    ax.text(x_pos + ancho/2, val + 8,
            f'+{int(crecimiento[i]*100)}%', ha='center', va='bottom', fontsize=9, color='gray')

# Ejes y etiquetas
ax.set_xticks(x)
ax.set_xticklabels(meses, fontsize=11)
ax.set_ylabel('Ventas mensuales (valor relativo)', fontsize=12)
plt.title('Ventas mensuales y tasa de crecimiento interanual (2º semestre 2023 vs 2022 / Ropa y calzado de moda en TikTok)', fontsize=14, pad=20)

# Leyenda
ax.legend(loc='upper left', fontsize=10)

# Caja de líneas discontinuas para resaltar de septiembre a noviembre
inicio_resaltado = x[3] - ancho*1.5
ancho_resaltado = (x[5] - x[3]) + ancho*3
rect = patches.Rectangle(
    (inicio_resaltado, 0), ancho_resaltado, max(datos_2023) * 1.1,
    linewidth=1.5, edgecolor='#e55322', linestyle='--', facecolor='none'
)
ax.add_patch(rect)

# Anotación de fuente de datos
fig.text(0.01, 0.01,
         'Fuente de datos: Plataforma de análisis de big data de marketing de nuevos negocios electrónicos de Youmi YouShu. El período de estadísticas es del 1 \nde junio al 31 de diciembre de 2022 y del 1 de junio al 31 de diciembre de 2023.',
         ha='left', va='bottom', fontsize=9)

# Cuadrícula
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)
ax.set_ylim(0, 140)
plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()