import matplotlib.pyplot as plt
import numpy as np

# Lista de métodos comunes de fraude telefónico
metodos_fraude = [
    "Adivina quién soy", "Falsificar la identidad de seguridad pública, fiscalía y tribunal\n'Ayudar en la investigación'",
    "Falsificar la identidad de\nTelecom/Ofice de Correos", "Reembolso de impuestos de consumo",
    "Fingir ser un conocido\ny defraudar", "Falso\nmensaje de texto de premio",
    "'Sonar una vez'\ny engañar para que se devuelva la llamada", "Enviar masivamente\nnúmero/nombre de tarjeta de crédito"
]
valores = np.array([15, 30, 10, 5, 20, 8, 7, 5])  # Usar proporciones de datos más realistas
total = sum(valores)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 8), facecolor='#f8f9fa')
fig.patch.set_alpha(0.9)  # Establecer la transparencia del lienzo

# Definir el efecto de explosión para resaltar la parte más grande
explode = [0.05 if v == max(valores) else 0 for v in valores]

# Esquema de colores personalizado (usar combinaciones de colores más brillantes)
colores = [
    '#ff6b6b', '#4ecdc4', '#ffd166', '#06d6a0',
    '#118ab2', '#ef476f', '#9381ff', '#ff9f1c'
]

# Dibujar un gráfico circular
wedges, texts, autotexts = ax.pie(
    valores,
    explode=explode,
    labels=None,  # No mostrar etiquetas temporalmente, mostrarlas a través de la leyenda
    autopct=lambda p: f'{p:.1f}%\n({int(p*total/100)})',  # Mostrar tanto el porcentaje como la cantidad real
    startangle=140,
    colors=colores,
    wedgeprops=dict(width=0.7, edgecolor='w', linewidth=1),  # Efecto de gráfico circular en forma de anillo
    pctdistance=0.85,  # Posición de la etiqueta del porcentaje
    textprops={'fontsize': 10, 'weight': 'bold', 'color': 'w'}
)

# Agregar un título y un subtítulo
ax.set_title("Distribución de métodos comunes de fraude telefónico", fontsize=18, fontweight="bold", pad=20)

# Agregar una leyenda
leyenda = ax.legend(
    wedges, metodos_fraude,
    title="Métodos de fraude",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=11,
    title_fontsize=13
)
leyenda.get_frame().set_alpha(0.8)  # Hacer el fondo de la leyenda semi - transparente

# Mejorar el diseño
plt.tight_layout(pad=4)  # Aumentar el margen
plt.subplots_adjust(right=0.75)  # Hacer espacio para la leyenda

# Mostrar el gráfico
plt.show()