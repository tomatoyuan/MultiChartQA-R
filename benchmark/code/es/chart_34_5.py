import matplotlib.pyplot as plt
import numpy as np

# Datos simulados, generalmente correspondientes a las categorías y tendencias en el gráfico original
categorias = ["Fragancias", "Camelia", "Sensación cero", "Estéril", "Cuidado de la piel", "Ácido hialurónico", "Tencel", "Hidratación", "Suspensión", "Aloe vera"]
datos_gmv = [71, 70, 20, 25, 20, 38, 26, 16, 32, 20]  # Datos de GMV (índice) simulados
datos_crecimiento = [0.10, 0.1, 0.08, 0.06, 0.05, 0.04, 0.03, 0.025, 0.02, 0.015]  # Datos de crecimiento año sobre año simulados

x = np.arange(len(categorias))  # Posiciones del eje x

# Crear un lienzo y un subgráfico, establecer el tamaño del gráfico
fig, ax1 = plt.subplots(figsize=(12, 7))

# Establecer el estilo de fondo - usar el estilo incorporado de Matplotlib en su lugar
plt.style.use('ggplot')

# Dibujar un gráfico de barras (GMV) - usar colores degradados
cmap = plt.cm.Blues
norm = plt.Normalize(min(datos_gmv), max(datos_gmv))
colores = cmap(norm(datos_gmv))

barras = ax1.bar(x, datos_gmv, width=0.6, color=colores, label='GMV (Índice)', edgecolor='black', linewidth=0.5)
ax1.set_ylabel('GMV (Índice)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Puntos de venta', fontsize=12, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, rotation=30, ha='right', fontsize=10)  # Rotar las etiquetas del eje x

# Agregar etiquetas de datos al gráfico de barras
for barra in barras:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2., altura + 1,
             f'{altura}', ha='center', va='bottom', fontsize=9)

# Crear un segundo eje y para dibujar un gráfico de línea (crecimiento año sobre año)
ax2 = ax1.twinx()
linea, = ax2.plot(x, datos_crecimiento, color='#FF7F50', marker='o', markersize=6,
                 linewidth=2, label='Tasa de crecimiento año sobre año')
ax2.set_ylabel('Tasa de crecimiento año sobre año', rotation=270, labelpad=18, fontsize=12, fontweight='bold')
ax2.set_ylim(0, 0.13)  # Aproximadamente correspondiente al rango de porcentaje en el gráfico original

# Agregar etiquetas de datos al gráfico de línea
for i, txt in enumerate(datos_crecimiento):
    ax2.annotate(f'{txt:.1%}', (x[i], datos_crecimiento[i]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center',
                 fontsize=9)

# Agregar un título y una leyenda
plt.title('Las 10 tasas de crecimiento más altas de los puntos de venta de ropa interior tecnológica de Douyin desde el lanzamiento de la nueva colección de primavera en 2025', fontsize=16, fontweight='bold', pad=20)

# Combinar las dos leyendas
lineas, etiquetas = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
ax2.legend(lineas + lineas2, etiquetas + etiquetas2, loc='upper right', frameon=True, shadow=True)

# Agregar líneas de cuadrícula
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.3)

# Ajustar los márgenes del gráfico
plt.tight_layout()

# Mostrar el gráfico
plt.show()