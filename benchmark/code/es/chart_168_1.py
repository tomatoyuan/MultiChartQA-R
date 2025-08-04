import matplotlib.pyplot as plt

# 数据
años = ['2019', '2020', '2021', '2022', '2023']
tamaño_del_mercado = [1199, 1221, 1404, 1415, 1549]
tasa_de_crecimiento = [3, 2, 15, 1, 9]

# Crear gráfico y ejes dobles
fig, ax1 = plt.subplots(figsize=(10, 6))

# Configurar el eje principal (eje izquierdo) - Gráfico de barras
barras = ax1.bar(años, tamaño_del_mercado, color='red', label='Tamaño del mercado\n (miles de millones de yuanes)')
ax1.set_ylabel('Tamaño del mercado \n(miles de millones de yuanes)', fontsize=12, color='red')
ax1.tick_params(axis='y', labelcolor='#000000')
ax1.set_ylim(0, 1900)
# Agregar etiquetas de datos al gráfico de barras
for barra in barras:
    valor_y = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width() / 2, valor_y + 10, f'{valor_y}', ha='center', va='bottom', fontsize=11, color='red')

# Crear el eje secundario (eje derecho) - Gráfico de línea
ax2 = ax1.twinx()
ax2.plot(años, tasa_de_crecimiento, color='#F6A700', marker='o', linewidth=2.5, label='Tasa de crecimiento interanual')
ax2.set_ylabel('Tasa de crecimiento interanual (%)', fontsize=14, color='#F6A700')
ax2.tick_params(axis='y', labelcolor='#000000')
ax2.set_ylim(0, 18)

# Agregar etiquetas de datos al gráfico de línea
for i, txt in enumerate(tasa_de_crecimiento):
    ax2.text(años[i], tasa_de_crecimiento[i] + 0.5, f'{txt}%', ha='center', va='bottom', fontsize=11, color='#F6A700')

# Agregar título y leyenda
plt.title('Tendencia del tamaño del mercado de papel higiénico en China', fontsize=14, pad=20)
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=12)
plt.text(0.5, -0.1, 'Fuente de datos: Asociación China de Papelera', fontsize=10, ha='center', transform=ax1.transAxes)
plt.tight_layout()
plt.show()