import matplotlib.pyplot as plt
import numpy as np

# 1. Extraer datos del gráfico
años = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
# Tamaño del mercado de varias categorías de alimentos prefabricados (en miles de millones de yuanes)
carne = [714, 829, 977, 1224, 1544, 2069, 2668, 3289]        # Carne
mariscos = [648, 733, 856, 1047, 1237, 1595, 2089, 2576]     # Mariscos
vegetales = [350, 480, 588, 676, 835, 1186, 1416, 1625]     # Vegetales
# Tamaño total del mercado (en miles de millones de yuanes)
total = [1712, 2042, 2421, 2947, 3616, 4850, 6173, 7490]
# Tasa de crecimiento interanual (%)
crecimiento = [19.3, 18.6, 21.7, 22.7, 34.2, 27.3, 21.3]

# 2. Dibujar gráfico combinado (gráfico de barras + gráfico de línea)
x = np.arange(len(años))  # Coordenadas del eje x
ancho = 0.2  # Ancho de las barras

fig, ax1 = plt.subplots(figsize=(14, 8))

# Dibujar gráfico de barras apiladas para tres categorías de alimentos prefabricados
base = np.zeros(len(años))
for i, (datos, etiqueta, color) in enumerate(zip(
    [carne, mariscos, vegetales], 
    ['Alimentos Prefabricados de Carne', 'Alimentos Prefabricados de Marisco', 'Alimentos Prefabricados de Verdura'], 
    ['#FF5722', '#FF9800', '#FFC107']
)):
    barras = ax1.bar(x, datos, ancho, bottom=base, label=etiqueta, color=color)
    # Anotar los valores de cada categoría
    for j, barra in enumerate(barras):
        altura = barra.get_height()
        if altura > 50:  # Solo anotar barras con altura suficiente para evitar sobrecrowding
            ax1.text(
                barra.get_x() + barra.get_width()/2., 
                base[j] + altura/2,
                f'{datos[j]}',
                ha='center', va='center',
                color='black', fontsize=8
            )
    base += datos

# Anotar valores del tamaño total del mercado
for i, val in enumerate(total):
    ax1.text(x[i], total[i] + 80, f'{val}', ha='center', fontsize=10, color='#333')

# Configurar eje y izquierdo (tamaño del mercado)
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuanes)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear eje y derecho para tasa de crecimiento interanual
ax2 = ax1.twinx()
ax2.plot(x[:-1], crecimiento, marker='o', color='#FDD835', label='Crecimiento Anual (%)', linewidth=2)

# Anotar valores de tasa de crecimiento
for i, val in enumerate(crecimiento):
    ax2.text(x[i], val + 1, f'{val}%', ha='center', fontsize=9, color='#FDD888')

ax2.set_ylabel('Crecimiento Anual (%)', fontsize=12, color='#FDD888')
ax2.tick_params(axis='y', labelcolor='#FDD888')
ax2.legend(loc='center right')

# 3. Configuración general del gráfico
plt.title('Tamaño del Mercado y Pronóstico de la Industria de Alimentos Prefabricados en China, 2019-2026', fontsize=14, pad=20)
plt.tight_layout()
plt.show()