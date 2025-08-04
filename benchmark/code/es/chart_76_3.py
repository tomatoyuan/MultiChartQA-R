import matplotlib.pyplot as plt

# Categorías de aplicaciones
etiquetas = [
    "Servicios de Video", "Comunicación y Chat", "Información Integral", 
    "Servicios de Juegos", "Redes Sociales", "Comercio Electrónico", 
    "Herramientas de Utilidad", "Otros"
]
# Proporción del tiempo de uso de cada aplicación (%)
tamaños = [43.9, 19.7, 7.3, 5.8, 4.1, 3.7, 3.6, 11.9]
# Colores para cada parte del gráfico circular
colores = [
    "#A4C639", "#A4D68C", "#BCE1A3", 
    "#87D3F2", "#74BCEF", "#F2D387", 
    "#F2B987", "#ECECEC"
]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 8))

# Dibujar un gráfico circular
porciones, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.1f%%', 
    startangle=140, colors=colores, 
    textprops={'color': 'black'}
)

# Embellir el texto de la anotación (ajustar tamaño, color, etc.)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

# Simular un borde exterior verde
for borde in ax.spines.values():
    borde.set_color('#A4C639')
    borde.set_linewidth(2)

# Establecer el título
ax.set_title("mUserTracker - Distribución del Tiempo de Uso de Aplicaciones de Usuarios en el Primer Trimestre de 2022", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()