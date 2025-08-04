import matplotlib.pyplot as plt
import numpy as np

# Datos sobre el número de campeones para cada apellido
data = {
    "Wang": 139, "Li": 132, "Liu": 127, "Zhang": 127, 
    "Chen": 113, "Yang": 63, "Huang": 58, "Zhao": 50, 
    "Zhou": 50, "Wu": 39
}

# Extraer apellidos y los recuentos correspondientes
apellidos = list(data.keys())
recuentos = list(data.values())

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(12, 7))

# Establecer columnas de color degradado
cmap = plt.cm.get_cmap('viridis', len(apellidos))
colores = [cmap(i) for i in range(len(apellidos))]
barras = ax.bar(apellidos, recuentos, color=colores, edgecolor='black', alpha=0.8)

# Añadir anotaciones numéricas
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura + 1.5,
            f'{altura}', ha='center', va='bottom', fontsize=12)

# Añadir título y etiquetas
ax.set_title('Lista de clasificación de apellidos de campeones', fontsize=18, pad=20)
ax.set_xlabel('Apellido', fontsize=14, labelpad=10)
ax.set_ylabel('Número de personas', fontsize=14, labelpad=10)

# Añadir líneas de cuadrícula
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Establecer el rango del eje y
ax.set_ylim(0, max(recuentos) * 1.1)

# Añadir color de fondo
ax.set_facecolor('#f8f9fa')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()