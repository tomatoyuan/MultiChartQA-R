import matplotlib.pyplot as plt
import numpy as np

# Datos
grupos_edad = ["Menos de 19", "25 - 34", "19 - 24", "35 - 49", "Más de 50"]
porcentajes = [11, 49, 20, 15, 5]
colores = ["#1f77b4", "#8dd3c7", "#bebada", "#fb8072", "#80b1d3"]  # Colores personalizados, se pueden ajustar

# Crear un gráfico de donut
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    porcentajes,
    labels=grupos_edad,
    autopct="%1.1f%%",  # Mostrar formato de porcentaje
    startangle=90,
    colors=colores,
    pctdistance=0.85,  # Distancia de las etiquetas de porcentaje desde el centro
    wedgeprops={"width": 0.4},  # Ancho del donut
)

# Agregar un círculo central (para que el donut sea más evidente)
circulo_central = plt.Circle((0, 0), 0.6, color="black", fc="white", linewidth=0)
ax.add_artist(circulo_central)

# Establecer el título
ax.set_title("Distribución de Grupos de Edad", fontsize=16, y=1.05)

# Mostrar el gráfico
plt.show()