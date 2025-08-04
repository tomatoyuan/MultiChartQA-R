import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
años = np.array([1950, 1960, 1970, 1980, 1990, 2016])
costos = np.array([10, 100, 500, 3000, 3000, 25])  # El valor para 2016 es un valor esquemático
etiquetas = [
    "10 yuanes\nEquivalente a 1/5 del ingreso mensual\n+ Certificado de organización",
    "100 yuanes\nEquivalente a 2 meses de ingresos\n+ Un conjunto de muebles",
    "500 yuanes\nEquivalente a 15 meses de ingresos\n+ Tres vueltas y un sonido",
    "3000 yuanes\nEquivalente a 30 meses de ingresos\n+ Refrigerador, televisión, lavadora",
    "3000 yuanes\nEquivalente a 30 meses de ingresos\n+ Tres joyas de oro, banquetes de boda, fotos de boda",
    ">250,000 yuanes\nEquivalente a 30 meses de ingresos"
]

# Crear una figura y ejes, aumentar el espacio superior
fig, ax = plt.subplots(figsize=(12, 8))
fig.subplots_adjust(top=0.85)  # Ajustar el espaciado superior

# Dibujar un gráfico de barras de color degradado (usando un mapa de colores)
cmap = plt.cm.viridis
norm = plt.Normalize(min(costos), max(costos))
colores = [cmap(norm(c)) for c in costos]
barras = ax.bar(np.arange(len(años)), costos, width=0.6, color=colores, edgecolor='gray')

# Establecer el título y las etiquetas
ax.set_title("Historia de los cambios en los costos de matrimonio en China", fontsize=18, fontweight='bold', pad=30)
ax.set_ylabel("Costo de matrimonio (Unidad: yuanes, el valor para 2016 es un valor esquemático)", fontsize=12)
ax.set_xticks(np.arange(len(años)))
ax.set_xticklabels(años, fontsize=11)

# Agregar líneas de cuadrícula y color de fondo
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f8f9fa')

# Optimizar las anotaciones de texto - Usar anotaciones con caja en lugar de anotaciones directas en las barras
for i, (barra, etiqueta) in enumerate(zip(barras, etiquetas)):
    altura = barra.get_height()
    ax.annotate(etiqueta,
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 15),  # Desplazamiento vertical
                textcoords="offset points",
                ha='center', va='bottom',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                fontsize=9)

# Agregar una leyenda
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=1, frameon=False)

plt.tight_layout()
plt.show()