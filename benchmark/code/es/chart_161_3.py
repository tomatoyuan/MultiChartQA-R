import matplotlib.pyplot as plt

# 数据
trimestres = ['23T1', '24T1']
categorias = ['Media', 'Marcas nacionales', 'Marcas internacionales']
datos = {
    'Media': [39, 39],
    'Marcas nacionales': [37, 43],
    'Marcas internacionales': [38, 37]
}
colores = ['#A0522D', '#FF8C00', '#FFA07A']  # Usar una combinación de colores similar a la imagen original

# Dibujar la gráfica
fig, ax = plt.subplots(figsize=(7, 5))
for idx, cat in enumerate(categorias):
    ax.plot(trimestres, datos[cat], marker='^', label=cat, color=colores[idx], linewidth=2)

# Agregar etiquetas de texto
for idx, cat in enumerate(categorias):
    for i, trimestre in enumerate(trimestres):
        ax.text(trimestre, datos[cat][i] + 0.5, f"{datos[cat][i]}%", color=colores[idx], ha='center', fontsize=12)

# Configuración de estilo
ax.set_ylim(35, 46)
ax.set_title("[Crema facial] Profundidad de promociones con regalos de las \n"
             "TOP15 marcas en 24T1 vs 23T1 (comercio electrónico principal)", fontsize=14, weight='bold')
ax.legend(loc='best')
ax.set_ylabel("Profundidad de promociones con regalos (%)")
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()