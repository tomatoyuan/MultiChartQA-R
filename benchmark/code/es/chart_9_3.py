import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
marcas = ['Apple', 'Huawei', 'Honor', 'Xiaomi', 'OPPO', 'vivo']
datos_tgi = [95, 105, 110, 95, 92, 95]  # Datos de atención (TGI)
datos_tasa_busqueda_bruta = [100, 110, 85, 87, 90, 89]  # Valores brutos del gráfico de línea de tasa de búsqueda
etiquetas_porcentaje_busqueda = [30, 44, 5, 7, 10, 8]  # Porcentajes reales de búsqueda a etiquetar
destacar_huawei = (1, 44)  # Etiqueta especial para Huawei (índice, valor de etiqueta)
destacar_honor = (2, 110)  # Etiqueta especial para Honor (índice, valor de etiqueta)

# Inicializar el gráfico y el eje doble
fig, ax1 = plt.subplots(figsize=(7, 5), dpi=100)
ax2 = ax1.twinx()

# Dibujar el gráfico de barras (TGI)
x = np.arange(len(marcas))  # Especificar claramente las posiciones de las marcas
grafico_barras = ax1.bar(x, datos_tgi, color='#4CAF50', width=0.6, edgecolor='white')
ax1.set_ylim(80, 120)
ax1.set_ylabel('(Atención/TGI)', color='#1f77b4', fontsize=9)
ax1.tick_params(axis='y', labelcolor='#1f77b4', labelsize=8, length=0)  # Eliminar las líneas de las marcas del eje y
ax1.set_xticks(x)  # Nuevo: Establecer explícitamente las posiciones de las marcas
ax1.set_xticklabels(marcas, fontsize=9)
ax1.tick_params(axis='x', length=0)  # Eliminar las líneas de las marcas del eje x

# Dibujar el gráfico de línea (Tasa de búsqueda)
grafico_linea, = ax2.plot(x, datos_tasa_busqueda_bruta, color='#FF9800', marker='o', markersize=5, linewidth=2)
ax2.set_ylim(80, 120)
ax2.set_ylabel('(Tasa de Búsqueda)', color='#FF9800', fontsize=9)
ax2.tick_params(axis='y', labelcolor='#FF9800', labelsize=8, length=0)  # Eliminar las líneas de las marcas del eje y

# Mapear el eje derecho a porcentajes
def mapear_a_porcentaje(tick):
    return ((tick - 80) / (120 - 80)) * 60

# Personalizar las marcas y etiquetas del eje derecho
ax2.set_yticks([80, 90, 100, 110, 120])
ax2.set_yticklabels([f'{mapear_a_porcentaje(tick):.0f}%' for tick in [80, 90, 100, 110, 120]], fontsize=8)

# Agregar líneas auxiliares discontinuas (referencia al gráfico original)
for y in [90, 100, 110]:
    ax1.axhline(y, color='gray', linestyle='--', linewidth=0.8)

# Etiquetas de datos especiales (Huawei 44%, Honor 110)
# Etiqueta para el punto del gráfico de línea de Huawei
ax2.text(destacar_huawei[0], datos_tasa_busqueda_bruta[destacar_huawei[0]], 
         f'{destacar_huawei[1]}%', 
         ha='center', va='bottom', fontsize=8, color='#FF9800',
         bbox=dict(facecolor='white', edgecolor='gray', pad=2, alpha=0.8))
# Etiqueta para el gráfico de barras de Honor
ax1.text(destacar_honor[0], datos_tgi[destacar_honor[0]] + 1, 
         f'{destacar_honor[1]}', 
         ha='center', va='bottom', fontsize=8, color='black',
         bbox=dict(facecolor='white', edgecolor='gray', pad=2, alpha=0.8))

# Título y anotación
plt.title('Atención (TGI) y Tasa de Búsqueda de Usuarios de Principales Marcas de Teléfonos Móviles a Nuevos Productos Nacionales', fontsize=10, fontweight='bold', pad=15)

texto_anotacion = (
    'Nota: Durante el período de estadísticas de nuestros datos (2019 - 2020), la marca Honor no estaba independiente de Huawei.\n'
    'TGI: Mide la atención. Un valor superior a 100 significa que la atención del grupo de usuarios es mayor que el nivel promedio.'
)
plt.figtext(0.12, 0.01, texto_anotacion, fontsize=8, color='gray', wrap=True)

# Leyenda y optimización del diseño
ax1.legend([grafico_barras, grafico_linea], ['Atención/TGI', 'Tasa de Búsqueda'], 
           loc='upper left', fontsize=8, frameon=True, facecolor='white')
plt.tight_layout(pad=3)

# Eliminar el borde del gráfico
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

plt.show()