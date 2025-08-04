import matplotlib.pyplot as plt
import numpy as np

# Datos para el nuevo gráfico
etiquetas = ["Dificultad para mejorar el ROI de la comunicación de marketing", "Dificultad para medir y verificar la efectividad", "Fragmentación de los medios"]
# Datos de proporción para cada categoría (ya que es un solo grupo de datos, use una matriz unidimensional directamente)
valores = np.array([62, 54, 50])  
# Esquema de colores (que coincida con el tono de color de la imagen original, se puede ajustar)
colores = ['#4C72B0', '#818181', '#A9A9A9']  

# Crear un lienzo y un subgráfico, establecer el tamaño del gráfico
fig, ax = plt.subplots(figsize=(8, 4))  

# Dibujar un gráfico de barras horizontales (datos de un solo grupo, no se requiere apilamiento)
for i, (etiqueta, valor, color) in enumerate(zip(etiquetas, valores, colores)):
    barra = ax.barh(etiqueta, valor, color=color, alpha=0.9, edgecolor='w', linewidth=0.5)
    
    # Anotar el porcentaje al final de la barra
    ax.text(
        valor + 1,  # El texto está en el lado derecho de la barra, la distancia se puede ajustar
        barra[0].get_y() + barra[0].get_height()/2,
        f"{valor}%", 
        ha='left', 
        va='center',
        fontweight='bold',
        fontsize=10
    )

# Establecer el título
ax.set_title('Desafíos de selección de medios de los anunciantes en 2021', fontsize=14, fontweight='bold', pad=20)  

# Establecer las etiquetas (el eje x representa el porcentaje, no se necesita una etiqueta adicional para el eje y, por lo que está comentado)
ax.set_xlabel('Porcentaje (%)', fontsize=12, labelpad=10)  
# ax.set_ylabel('Categoría', fontsize=12, labelpad=10)  # Descomente si necesita una etiqueta para el eje y

# Establecer el rango del eje x para que la visualización de los datos sea más razonable
ax.set_xlim(0, 70)  

# Establecer las líneas de cuadrícula (dirección del eje x, línea discontinua, semitransparente)
ax.grid(axis='x', linestyle='--', alpha=0.7)  

# Ocultar los bordes (puede mejorar la simplicidad)
for spine in ax.spines.values():
    spine.set_visible(False)

# Ajustar el diseño para una mejor visualización
plt.tight_layout()  

# Mostrar el gráfico
plt.show()