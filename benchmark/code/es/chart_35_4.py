import matplotlib.pyplot as plt

# Preparación de datos
categorias = [
    "Susceptibilidad a la fatiga", "Problemas de peso", "Problemas de piel", "Tracto gastrointestinal/digestivo",
    "Estado de ánimo ansioso/depresivo", "Presión arterial, azúcar y lípidos sanguíneos altos", "Problemas respiratorios", "Ninguno de los anteriores"
]
porcentajes = [53, 50, 48, 47, 44, 29, 19, 10]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras horizontales con colores degradados
colores = plt.cm.viridis([i/len(categorias) for i in range(len(categorias))])
barras = ax.barh(categorias, porcentajes, color=colores, edgecolor='gray', alpha=0.8)

# Añadir un título y etiquetas de los ejes
ax.set_title("Aspectos específicos del aumento de los problemas de salud física de los consumidores en el último año", fontsize=16, pad=15)
ax.set_xlabel("Porcentaje (%)", fontsize=14, labelpad=10)
ax.set_ylabel("Tipos de problemas de salud", fontsize=14, labelpad=10)

# Establecer el rango y las marcas del eje x
ax.set_xlim(0, max(porcentajes) * 1.1)  # Ampliar ligeramente el rango del eje x
ax.set_xticks(range(0, 60, 10))

# Añadir líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Añadir etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height()/2,
            f'{ancho}%', ha='left', va='center', fontsize=12)

# Emprolijar el gráfico
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', which='major', labelsize=12)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()