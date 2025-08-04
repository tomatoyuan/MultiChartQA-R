import matplotlib.pyplot as plt

# Categorías de eficacia y sus proporciones
etiquetas = ['Mejora la inmunidad', 'Combate la fatiga', 'Protección hepática', 'Cuidado visual', 'Ayuda a dormir', 'Otros']
tamaños = [42, 15, 13, 8, 2, 20]
colores = ['#0057FF', '#7DECF6', '#00B388', '#93B6FF', '#CED6F8', '#EDEDED']

# Dibujar el gráfico circular
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_porcentaje = ax.pie(
    tamaños, labels=etiquetas, colors=colores, autopct='%1.0f%%',
    startangle=90, textprops={'fontsize': 10}, pctdistance=0.8
)

# Establecer el título
ax.set_title("Distribución de eficacia de nuevos productos de suplementos dietéticos en\n el primer semestre de 2023", fontsize=14, fontweight='bold')

# Agregar la explicación de la fuente de datos
plt.figtext(
    0.5, -0.1,
    'Nota: "Combate la fatiga" corresponde a la función de "Aliviar la fatiga física" en los suplementos dietéticos,\n'
    ' "Protección hepática" corresponde a la función de "Proteger el hígado de daños químicos" y "Cuidado visual"\n'
    ' corresponde a la función de "Aliviar la fatiga visual".\nFuente de datos: Administración General de Mercado de China, recopilación de información pública',
    wrap=True, horizontalalignment='center', fontsize=9
)

plt.tight_layout()
plt.show()