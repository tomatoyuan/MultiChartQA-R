import matplotlib.pyplot as plt
import numpy as np

# Etiquetas de períodos de tiempo
etiquetas = ["00:00", "05:00", "10:00", "15:00", "20:00"]
# Datos de proporción simulados (pueden ser reemplazados según necesidades reales, los valores aquí son solo de demostración)
tamaños = [10, 10, 50, 15, 15]  
# Espacio en el gráfico de dona (para que la dona sea más obvia), aquí se establece uniformemente en 0.3, se puede ajustar
separacion = [0.3] * len(etiquetas)  

fig, ax = plt.subplots()

# Dibujar un gráfico de dona, wedgeprops controla el ancho y otros estilos de la dona
ax.pie(
    tamaños,
    explode=separacion,
    labels=etiquetas,
    autopct="%1.1f%%",  # Mostrar porcentaje
    startangle=90,      # Ángulo de inicio
    wedgeprops={"width": 0.3, "edgecolor": "white"},  # Ancho de la dona, color del borde
    textprops={"fontsize": 12}  # Tamaño de fuente del texto
)
ax.set_title("¿Cuándo la gente quiere más 'comprar hasta desmayarse' en el '11.11'?", fontsize=16, fontweight="bold")

# Mantener el gráfico de pastel circular (para evitar estiramiento y distorsión)
ax.axis("equal")  

plt.show()