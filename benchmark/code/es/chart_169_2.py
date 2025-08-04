import matplotlib.pyplot as plt

# Datos
etiquetas = [
    "El soporte de la tecnología de \n"
    "cuidado de la piel puede hacer que \n"
    "los componentes funcionen mejor",
    "No me importa la tecnología que"
    " contiene el producto\n"
    "Todavía me centro en los componentes",
    "No he prestado atención al concepto \n"
    "de “cuidado de la piel con tecnología”"
]
tamaños = [83, 12, 5]
colores = ['#FFB6C1', '#FFCCE5', '#FFE6F0']  # Gradiente de tonos rosados
explode = (0.05, 0, 0)  # Resaltar el primer segmento

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(7, 5))
segmentos, textos, textos_automaticos = ax.pie(
    tamaños,
    explode=explode,
    labels=etiquetas,
    colors=colores,
    autopct='%1.0f%%',
    startangle=140,
    textprops={'fontsize': 12},
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
)

ax.axis('equal')  # Asegurar que el gráfico circular sea redondo
plt.title("Encuesta sobre la opinión de las consumidoras femeninas contemporáneas \nsobre la idea de “cuidado de la piel con tecnología”", fontsize=14, weight='bold', pad=30)
plt.tight_layout()
plt.show()