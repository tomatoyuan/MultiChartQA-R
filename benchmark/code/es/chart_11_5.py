import matplotlib.pyplot as plt
import numpy as np

# Datos (Nombres de carreras + Índice de búsqueda)
carreras = [
    "Bioingeniería", "Economía y Comercio Internacional", "Ingeniería de Comunicación", 
    "Finanzas", "Administración de Empresas", "Economía", 
    "Aplicaciones de Computación", "Automática Eléctrica"
]
indice_busqueda = [323, 712, 1060, 1374, 1241, 945, 581, 447]

# Invertir el orden de los datos (para tener "Bioingeniería" en la parte superior, consistente con la figura original)
carreras = carreras[::-1]
indice_busqueda = indice_busqueda[::-1]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
colores = ["#99D8C9", "#4ECDC4", "#239B56", "#E74C3C", "#F39C12", "#F1C40F", "#3498DB", "#9B59B6"]
ax.barh(carreras, indice_busqueda, color=colores, height=0.7)

# Agregar etiquetas del índice de búsqueda
for i, idx in enumerate(indice_busqueda):
    ax.text(idx + 20, i, str(idx), va="center", fontsize=10, fontweight="bold")

# Establecer el título
ax.set_title("¿Qué le pasó a las carreras una vez populares?", fontsize=14, fontweight="bold", pad=20, loc="left")

# Ocultar los bordes superior, derecho y las marcas del eje x
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks([])

# Ajustar el tamaño de fuente de las marcas del eje y
ax.tick_params(axis='y', labelsize=11)

# Establecer el rango del eje x para dejar espacio para las etiquetas
ax.set_xlim(0, max(indice_busqueda) + 200)

plt.tight_layout()
plt.show()