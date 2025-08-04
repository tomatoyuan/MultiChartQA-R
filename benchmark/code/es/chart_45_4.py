import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['Protector solar básico', 'Ropa de protección solar funcional y elegante', 'Conjuntos de protector solar/lentes de protección solar de lujo']
rangos_precio = [
    ['Menos de 100 yuan', '100 - 150 yuan'],
    ['150 - 200 yuan', '200 - 250 yuan'],
    ['250 - 300 yuan', '300 - 500 yuan', 'Más de 500 yuan']
]
porcentajes = [
    [3, 15],
    [29, 24],
    [16, 10, 3]
]

# Asegurarse de que todos los rangos de precio tengan leyendas
todos_rangos_precio = ['Menos de 100 yuan', '100 - 150 yuan', '150 - 200 yuan', '200 - 250 yuan', '250 - 300 yuan', '300 - 500 yuan', 'Más de 500 yuan']

# Establecer parámetros gráficos
ancho_barra = 0.6
posiciones_y = np.arange(len(categorias))

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Definir una lista de colores para asegurar el mismo color para cada rango de precio
colores = plt.cm.tab20.colors

# Dibujar un gráfico de barras horizontales
fondos = [0] * len(categorias)
for i, (rangos, porcs) in enumerate(zip(rangos_precio, porcentajes)):
    for j, (rango_precio, porcentaje) in enumerate(zip(rangos, porcs)):
        indice_color = todos_rangos_precio.index(rango_precio)
        etiqueta = rango_precio  # Establecer una etiqueta para cada rango de precio
        ax.barh(posiciones_y[i], porcentaje, ancho_barra, left=fondos[i], 
                label=etiqueta, alpha=0.8, color=colores[indice_color])
        fondos[i] += porcentaje

# Añadir etiquetas de datos
for i, (rangos, porcs) in enumerate(zip(rangos_precio, porcentajes)):
    fondo_actual = 0
    for j, (rango_precio, porcentaje) in enumerate(zip(rangos, porcs)):
        if porcentaje > 0:  # Solo añadir etiquetas cuando el porcentaje sea mayor que 0
            ax.text(fondo_actual + porcentaje/2, i, f"{porcentaje}%", 
                    ha='center', va='center', color='black', fontweight='bold')
        fondo_actual += porcentaje

# Establecer atributos del gráfico
ax.set_yticks(posiciones_y)
ax.set_yticklabels(categorias)
ax.set_xlabel('Porcentaje (%)')
ax.set_title('Tendencia de los consumidores en los rangos de precios de compra de ropa y suministros de protección solar')

# Ajustar la leyenda
manijas, etiquetas = ax.get_legend_handles_labels()
# Crear elementos únicos de la leyenda
unicos = [(h, l) for i, (h, l) in enumerate(zip(manijas, etiquetas)) if l not in etiquetas[:i]]
ax.legend(*zip(*unicos), loc='lower right')

# Mostrar líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()