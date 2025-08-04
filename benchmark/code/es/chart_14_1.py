import matplotlib.pyplot as plt
import numpy as np

# Nombres de los artículos esenciales de verano
etiquetas = ['Aire acondicionado', 'Protector solar', 'Paraguas', 'Traje de baño', 'Repelente de insectos', 'Ventilador eléctrico', 'Refrigerador', 'Sandía', 'Manta fresca']
# Datos de porcentaje de "poder de combate" correspondientes
valores = [73.15, 48, 35, 26, 10, 8.4, 7.8, 5, -7.9]

# Ordenamiento de los datos (en orden ascendente, pero se invertirá al graficar para que los valores más grandes estén en la parte superior)
datos_ordenados = sorted(zip(valores, etiquetas), reverse=False)
valores, etiquetas = zip(*datos_ordenados)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Establecer barras de color degradado (color más oscuro para valores más grandes)
colores = plt.cm.Oranges(np.linspace(0.4, 0.9, len(valores)))

# Dibujar un gráfico de barras horizontales embellecido
barras = ax.barh(etiquetas, valores, color=colores, edgecolor='gray', linewidth=0.8)

# Establecer el rango del eje X (Modificación clave: extender negativamente hasta -15)
ax.set_xlim(-15, max(valores) + 5)

# Agregar líneas de cuadrícula de fondo
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Establecer el título y las etiquetas
ax.set_title('Ranking de "poder de combate" de los artículos esenciales de verano', fontsize=16, pad=15)
ax.set_xlabel('Porcentaje de "poder de combate"', fontsize=12, labelpad=10)

# Ajustar los estilos de las marcas y las etiquetas
ax.tick_params(axis='both', which='major', labelsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Optimizar las posiciones de las etiquetas de datos (ajustar según el nuevo rango del eje X)
for barra, valor in zip(barras, valores):
    # Ajustar la posición de las etiquetas de valores positivos y aumentar el espaciado
    x_pos = valor + 0.8 if valor > 0 else valor - 0.8
    # Ajustar la posición de las etiquetas de valores negativos según el rango del eje X
    ax.text(x_pos,
            barra.get_y() + barra.get_height()/2,
            f'{valor}%',
            ha='left' if valor > 0 else 'right',
            va='center',
            fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# Agregar una línea de referencia (en la posición 0)
ax.axvline(x=0, color='black', linestyle='-', alpha=0.3)

# Agregar un color de fondo al área negativa (embellecimiento opcional)
ax.axvspan(-15, 0, alpha=0.05, color='lightgray')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()