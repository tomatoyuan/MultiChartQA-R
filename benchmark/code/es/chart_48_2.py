import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Grupos de edad
grupos_edad = [
    "50-54 años", "55-59 años", "60-64 años", "65-69 años", 
    "70-74 años", "75-79 años", "80-84 años", "85-89 años", 
    "90-94 años", "95 años y mayores"
]
# Población por grupo de edad (personas)
poblacion = [127635, 117482, 71964, 79964, 58782, 35928, 22434, 12542, 4297, 929]
# Proporción de la población nacional (%)
proporcion = [8.84, 8.14, 4.98, 5.54, 4.07, 2.49, 1.55, 0.87, 0.30, 0.06]

x = np.arange(len(grupos_edad))  # Coordenadas del eje x
ancho = 0.35  # Ancho de las barras

# Crear un lienzo y ejes primario y secundario
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Dibujar un gráfico de barras de la población (gradiente azul oscuro)
cmap1 = plt.cm.Blues
norm1 = plt.Normalize(min(poblacion), max(poblacion))
colores1 = [cmap1(norm1(valor)) for valor in poblacion]
rects1 = ax1.bar(x - ancho/2, poblacion, ancho, label='Población por grupo de edad (personas)', color=colores1)

# Dibujar un gráfico de barras de la proporción (gradiente verde oscuro)
cmap2 = plt.cm.Greens
norm2 = plt.Normalize(min(proporcion), max(proporcion))
colores2 = [cmap2(norm2(valor)) for valor in proporcion]
rects2 = ax2.bar(x + ancho/2, proporcion, ancho, label='Proporción de la población nacional (%)', color=colores2)

# Establecer etiquetas de los ejes y título
ax1.set_ylabel('Población (en diez miles de personas)', fontsize=13, color='#004D40')
ax1.set_xlabel('Grupos de edad', fontsize=13)
ax1.set_title('Distribución de edad y proporción de la población de 50 años y mayores en China en 2022', fontsize=16, pad=20, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(grupos_edad, rotation=30, ha='center', fontsize=12)

# Establecer el formato del eje y
def miles_formatter(x, pos):
    return f'{x/10000:.1f}'
ax1.yaxis.set_major_formatter(FuncFormatter(miles_formatter))

# Agregar líneas de cuadrícula
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle=':', alpha=0.5)

# Agregar etiquetas numéricas a cada barra (con separadores de miles)
def agregar_etiquetas(rects, ax, es_porcentaje=False):
    for rect in rects:
        altura = rect.get_height()
        if es_porcentaje:
            etiqueta = f'{altura:.2f}%'
        else:
            etiqueta = f'{altura:,}'
        ax.annotate(etiqueta,
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 5),  # Distancia vertical de la etiqueta desde la barra
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

agregar_etiquetas(rects1, ax1)
agregar_etiquetas(rects2, ax2, es_porcentaje=True)

# Embelezar la leyenda
lineas, etiquetas = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
ax2.legend(lineas + lineas2, etiquetas + etiquetas2, loc='upper right', frameon=True, framealpha=0.9, shadow=True)

# Ajustar el diseño
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Dejar espacio en la parte inferior y superior
plt.show()