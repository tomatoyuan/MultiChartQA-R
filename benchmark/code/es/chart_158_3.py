import matplotlib.pyplot as plt

# 数据
etiquetas = [
    'Aumento de líneas finas/arrugas', 'Disminución de la elasticidad de la piel', 'Exceso de secreción de grasa', 'Piel áspera y amarillenta', 'Pores dilatados', 'Disminución del brillo',
    'Pobre aspecto facial', 'Disminución de la humedad de la piel', 'Desigualdad de tono de piel', 'Apariencia de manchas', 'Espinillas y acné', 'Piel sensible', 'Edema crónico'
]
porcentajes = [63, 60, 59, 58, 54, 53, 53, 52, 40, 35, 33, 25, 22]

# Establecer colores
colores = ['#FFCC00' if i < 4 else '#673AB7' for i in range(len(etiquetas))]

x = range(len(etiquetas))
fig, ax = plt.subplots(figsize=(12, 6))
barras = ax.bar(x, porcentajes, color=colores)

# Agregar etiquetas de porcentaje sobre las barras
for i, barra in enumerate(barras):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura + 1,
            f'{porcentajes[i]}%', ha='center', va='bottom', fontsize=11)

# Establecer etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, fontsize=10, rotation=30, ha='right')

# Título
ax.set_title('Más del 60% de las personas notan aumento de líneas finas/arrugas\n'
             ' y disminución de la elasticidad de la piel causadas por problemas de sueño',
             fontsize=14, weight='bold',pad=50)

ax.set_ylim(0, 75)
ax.set_ylabel('Porcentaje (%)', fontsize=12)

x_medio = (0 + 1) / 2
ax.text(x_medio-1.3, 74, 'Problema principal de\notras generaciones\nexcluyendo los post-2000',
        ha='center', va='bottom', fontsize=10,
        bbox=dict(facecolor='#E0E0E0', edgecolor='gray', boxstyle='round,pad=0.3'))

ax.text(1.5, 72, 'Más evidente en\npost-2000, post-1995, \npost-1990',
        ha='center', va='bottom', fontsize=10,
        bbox=dict(facecolor='#E0E0E0', edgecolor='gray', boxstyle='round,pad=0.3'))

# Nota al pie de página de la fuente de los datos
plt.figtext(0.5, -0.08,
            'Fuente de datos: Encuesta de CBNData en julio de 2024\nQ15. ¿Qué efectos cree que los problemas de sueño (acostarse tarde o mala calidad de sueño) han tenido en su piel?',
            wrap=True, ha='center', fontsize=9, color='gray')

# Mejorar la apariencia
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='y', left=True)

plt.tight_layout()
plt.show()