import matplotlib.pyplot as plt

# Gráfico 4: Distribución de las solicitudes de platos de comida de delivery
etiquetas = [
    "La comida es fresca \n"
    "y la calidad de los \n"
    "ingredientes está garantizada",
    "Es equilibrada nutricionalmente\n"
    " y bien combinada",
    "Tiene una textura variada \n"
    "y un buen sabor",
    "Hay una amplia \n"
    "variedad para elegir",
    "La temperatura de la\n"
    " comida se mantiene bien",
    "La comida se puede personalizar",
    "Hay una cantidad suficiente\n"
    " para llenar el estómago"
]
valores = [77.2, 68.2, 68.0, 48.6, 31.9, 31.8, 23.5]

colores = plt.cm.Greens_r([0.2 + i*0.1 for i in range(len(valores))])

fig, ax = plt.subplots(figsize=(8, 5.5))
barras = ax.barh(etiquetas, valores, color=colores)

# Agregar etiquetas de valores
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1.5, barra.get_y() + barra.get_height()/2,
            f'{ancho:.1f}%', va='center', fontsize=10)

# Configuración del gráfico
ax.set_xlim(0, 85)
ax.set_xlabel("Porcentaje (%)", fontsize=12)
ax.set_title("Distribución de las solicitudes de platos de comida de delivery", fontsize=14, weight='bold')
plt.gca().invert_yaxis()  # Invertir el eje y para que el valor máximo esté en la parte superior

# Fuente de los datos

plt.tight_layout()
plt.show()