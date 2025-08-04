import matplotlib.pyplot as plt
import numpy as np

# Datos
ciudades = ["Beijing", "Chengdu", "Shanghai", "Hangzhou", "Shenzhen"]
proporciones_busqueda = [4.3, 3.4, 2.9, 2.5, 2.5]

# Crear un lienzo y un sub - gráfico
plt.figure(figsize=(10, 6), dpi=300)
ax = plt.subplot(111)

# Establecer un gráfico de barras de color degradado
colores = plt.cm.viridis(np.linspace(0.3, 0.8, len(ciudades)))
barras = plt.bar(ciudades, proporciones_busqueda, color=colores, width=0.6, edgecolor='black', linewidth=0.8)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura + 0.05,
             f'{altura}%', ha='center', va='bottom', fontweight='bold')

# Agregar un título y etiquetas de ejes
plt.title("Las 5 principales ciudades de búsqueda en la industria de la formación profesional en mayo", fontsize=16, fontweight='bold')
plt.xlabel("Ciudad", fontsize=12)
plt.ylabel("Proporción de búsqueda (%)", fontsize=12)

# Establecer el rango y las divisiones del eje
plt.ylim(0, max(proporciones_busqueda) * 1.1)
plt.yticks(np.arange(0, 5, 0.5))

# Agregar líneas de cuadrícula
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar un color de fondo
ax.set_facecolor('#f8f9fa')

# Ajustar el borde
for spine in ax.spines.values():
    spine.set_color('#cccccc')

# Agregar una leyenda
plt.legend([barras[0]], ['Proporción de búsqueda'], loc='upper right')

# Optimizar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()