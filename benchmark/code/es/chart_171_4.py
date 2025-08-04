import matplotlib.pyplot as plt
import numpy as np

# Datos
bandas_de_precio = ['Menos de 50 yuanes', '50 - 100 yuanes', '100 - 300 yuanes', 'Más de 300 yuanes']
valor_2022 = [0.30, 0.28, 0.27, 0.15]
valor_2023 = [v + d for v, d in zip(valor_2022, [0.09, -0.01, -0.03, -0.04])]
cambio_de_valor = ['+9%', '-1%', '-3%', '-4%']

# Dibujo del gráfico
fig, ax = plt.subplots(figsize=(7, 5))
y = np.arange(len(bandas_de_precio))
altura_de_la_barra = 0.35

# Gráfico de barras horizontales
ax.barh(y - altura_de_la_barra / 2, valor_2022, height=altura_de_la_barra, color='#e55322', label='2H 2022')
ax.barh(y + altura_de_la_barra / 2, valor_2023, height=altura_de_la_barra, color='black', label='2H 2023')

# Etiquetas de los valores
for i in range(len(bandas_de_precio)):
    ax.text(valor_2022[i] + 0.005, y[i] - altura_de_la_barra / 2,
            f'{int(valor_2022[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if valor_2022[i] > 0.3 else 'black')
    ax.text(valor_2023[i] + 0.005, y[i] + altura_de_la_barra / 2,
            f'{int(valor_2023[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if valor_2023[i] > 0.3 else 'black')
    ax.text(max(valor_2022[i], valor_2023[i]) + 0.03, y[i],
            cambio_de_valor[i], va='center', fontsize=10)

# Estilo
ax.set_title('Cambio en la proporción de ventas por banda de precio\n (2H 2023 vs / Ropa, calzado y accesorios en Douyin)', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(bandas_de_precio, fontsize=11)
ax.set_xlim(0, max(valor_2022) + 0.2)
ax.invert_yaxis()
ax.legend(loc='lower right', fontsize=9)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

# Fuente de los datos
fig.text(0.01, -0.01,
         'Fuente de datos: Plataforma de análisis de grandes datos de marketing del nuevo comercio electrónico de\n'
         ' Youmi Youshu. El período de estadísticas es del 1.6.2022 al 31.12.2022 y del 1.6.2023 al 31.12.2023.',
         ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()