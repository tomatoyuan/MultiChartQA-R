import matplotlib.pyplot as plt
import numpy as np

# Definición de datos, distribución de la cantidad de proyectos y distribución del monto de los proyectos
etiquetas = ["Bancos", "Seguros", "Valores", "Otros"]
tamaños_cantidad = [53, 12, 15, 20]  # Distribución de la cantidad de proyectos, simulada aproximadamente
tamaños_monto = [56, 8, 17, 19]  # Distribución del monto de los proyectos, simulada aproximadamente
# Configuración de colores, lo más cercano posible a la imagen original
colores = ["greenyellow", "green", "limegreen", "lightseagreen"]

# Crear un lienzo y subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Dibujar un gráfico circular de la distribución de la cantidad de proyectos
ax1.pie(tamaños_cantidad, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
ax1.set_title('Distribución de la cantidad de proyectos')

# Dibujar un gráfico circular de la distribución del monto de los proyectos
ax2.pie(tamaños_monto, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
ax2.set_title('Distribución del monto de los proyectos')

# Agregar un título principal
fig.suptitle('Distribución de las ofertas ganadoras para modelos de gran escala de la industria financiera en 2024', fontsize=14)

plt.tight_layout()
plt.show()