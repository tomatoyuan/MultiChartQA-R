import matplotlib.pyplot as plt
import numpy as np

# Datos
bandas_precio = ['Menos de 50 yuanes', '50 - 100 yuanes', '100 - 300 yuanes', 'Más de 300 yuanes']
volumen_2022 = [0.38, 0.25, 0.22, 0.15]
volumen_2023 = [v + d for v, d in zip(volumen_2022, [0.12, -0.06, -0.05, -0.01])]
cambio_volumen = ['+12%', '-6%', '-5%', '-1%']

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(7, 5))
y = np.arange(len(bandas_precio))
altura_barra = 0.35

# Gráfico de barras horizontales
ax.barh(y - altura_barra / 2, volumen_2022, height=altura_barra, color='#e55322', label='2H 2022')
ax.barh(y + altura_barra / 2, volumen_2023, height=altura_barra, color='black', label='2H 2023')

# Anotación de valores
for i in range(len(bandas_precio)):
    ax.text(volumen_2022[i] + 0.005, y[i] - altura_barra / 2,
            f'{int(volumen_2022[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if volumen_2022[i] > 0.3 else 'black')
    ax.text(volumen_2023[i] + 0.005, y[i] + altura_barra / 2,
            f'{int(volumen_2023[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if volumen_2023[i] > 0.3 else 'black')
    ax.text(max(volumen_2022[i], volumen_2023[i]) + 0.03, y[i],
            cambio_volumen[i], va='center', fontsize=10)

# Estilo
ax.set_title('Cambio en la proporción de ventas por banda de precios\n (2º semestre de 2023 año sobre año / Ropa, calzado y accesorios de moda en Douyin)', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(bandas_precio, fontsize=11)
ax.set_xlim(0, max(volumen_2023) + 0.2)
ax.invert_yaxis()
ax.legend(loc='lower right', fontsize=9)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

# Fuente de los datos
fig.text(0.2, -0.03,
         'Fuente de datos: Plataforma de análisis de grandes datos de marketing de nuevos \n'
         'negocios electrónicos de Youmi Youshu. El período de estadísticas es del 1 de \n'
         'junio al 31 de diciembre de 2022 y del 1 de junio al 31 de diciembre de 2023.',
         ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()