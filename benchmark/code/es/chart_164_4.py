import matplotlib.pyplot as plt

# 数据
etiquetas = [
    "Funcionalidad + moda + comodidad \n"
    "son igualmente importantes\n"
    "Se plantea la demanda de multifunción",
    "Funcionalidad como prioridad, \n"
    "moda y comodidad como secundarias",
    "Solo se requiere funcionalidad\n"
    " y rendimiento deportivo",
    "Solo se preocupan por la \n"
    "información del producto, \n"
    "como la categoría y la marca",
    "Solo se preocupan por la moda"
]
tamaños = [48, 26, 15, 5, 5]
colores = ['#FFB84C', '#FBC374', '#FFDCA8', '#FFE9C1', '#FFF3DC']

# Dibujar el gráfico circular
plt.figure(figsize=(8, 6))
sectores, textos, textos_automaticos = plt.pie(
    tamaños,
    labels=etiquetas,
    colors=colores,
    startangle=140,
    autopct='%1.0f%%',
    textprops={'fontsize': 10}
)

# Título y explicación de la fuente de datos
plt.title('Distribución de las demandas de los consumidores para la ropa exterior de lujo (%)', fontsize=14)
plt.figtext(0.5, 0.02, "Fuente de datos: Encuesta de CBNData en mayo de 2024; N = 1000", ha="center", fontsize=10)

plt.tight_layout()
plt.show()