import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Contenido de agua / Permeabilidad al oxígeno', 'Composición del material', 'Parámetros de uso', 'Lugar de origen', 'Programa de reemplazo', 'Proceso de coloración', 'Reputación de la marca', 'Nivel de precio', 'Servicios relacionados', 'Empaquetado y almacenamiento']
valores = [52, 52, 46, 45, 43, 43, 42, 41, 40, 35]

# Definir posiciones en el eje y
pos_y = np.arange(len(etiquetas))

# Esquema de colores de gradiente optimizado (de azul oscuro a azul claro)
colores = plt.cm.Blues(np.linspace(0.4, 0.9, len(etiquetas)))

# Crear una figura (aumentar el tamaño)
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras horizontales (aumentar márgenes y transparencia)
barras = ax.barh(pos_y, valores, color=colores, alpha=0.85, edgecolor='gray', linewidth=0.5)

# Establecer etiquetas en el eje y (aumentar el espaciado de las etiquetas)
ax.set_yticks(pos_y)
ax.set_yticklabels(etiquetas, fontsize=10)

# Establecer etiqueta del eje x y título
ax.set_xlabel('Porcentaje de atención', fontsize=12)
ax.set_title('Dimensiones profesionales de la atención de los consumidores a las lentes de contacto', fontsize=14, pad=15)

# Optimizar las etiquetas numéricas (aumentar el tamaño de fuente y el color)
for i, v in enumerate(valores):
    ax.text(v + 1, i, f'{v}%', va='center', fontsize=10, color='black')

# Agregar líneas de cuadrícula (cuadrícula más clara)
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Establecer el rango del eje x (aumentar márgenes)
ax.set_xlim(0, max(valores) * 1.1)

# Embelezar el borde (ocultar los bordes superior y derecho)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()