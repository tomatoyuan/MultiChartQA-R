import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
periodos = ['Jun - Ago 2022', 'Sep - Dic 2022', 'Ene - Mar 2023', 'Abr - Jun 2023', 'Jul - Sep 2023', 'Oct - Dic 2023']
episodios = [420, 1402, 1848, 2686, 3321, 3532]  # Número de episodios emitidos (eje derecho)
titulos = [19, 64, 83, 116, 150, 153]           # Número de títulos emitidos (eje izquierdo)

x = np.arange(len(periodos))
ancho_barra = 0.5

# Crear la figura
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Gráfico de barras (eje izquierdo): Número de títulos emitidos
barras = ax1.bar(x, titulos, width=ancho_barra, color='#ff2d55', label='Número de títulos emitidos')

# Agregar etiquetas en la parte superior de las barras
for i, val in enumerate(titulos):
    ax1.text(x[i], val - 12, str(val), ha='center', fontsize=10, color='black')

# Gráfico de línea (eje derecho): Número de episodios emitidos
ax2.plot(x, episodios, color='#586173', linewidth=2.5, marker='o', markersize=25, label='Número de episodios emitidos', zorder=5)

# Agregar etiquetas numéricas en los nodos
for i, val in enumerate(episodios):
    ax2.text(x[i], val, str(val), ha='center', va='center', fontsize=10, color='white', zorder=6)

# Configurar los ejes y las etiquetas
ax1.set_xticks(x)
ax1.set_xticklabels(periodos, fontsize=11)
ax1.set_ylabel('Número de títulos emitidos', fontsize=12, color='#ff2d55')
ax2.set_ylabel('Número de episodios emitidos', fontsize=12, color='#586173')

ax1.set_ylim(0, 200)     # Eje izquierdo (número de títulos)
ax2.set_ylim(0, 4000)    # Eje derecho (número de episodios)

# Título
plt.title('Junio 2022 - Diciembre 2023 Número de licencias de emisión de micro - dramas de la \nAdministración de Radio, Televisión y Producción Audiovisual', fontsize=14, fontweight='bold', pad=20)

# Combinar las leyendas de ambos ejes
lineas1, etiquetas1 = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
fig.legend(lineas1 + lineas2, etiquetas1 + etiquetas2, loc='lower right', fontsize=10)

# Cuadrícula y mejoras visuales
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

fig.text(0.01, -0.1, '  ', fontsize=9, ha='left')


plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()