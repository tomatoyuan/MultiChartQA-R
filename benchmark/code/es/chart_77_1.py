import matplotlib.pyplot as plt

# Categorías de cambio de presupuesto
etiquetas = ["Disminuyó significativamente", "Disminuyó ligeramente", "Básicamente sin cambios", "Aumentó ligeramente", "Aumentó significativamente"]
# Proporción de cada categoría (%)
tamaños = [10.5, 40.8, 34.9, 12.5, 1.3]
# Colores para cada parte del gráfico circular
colores = ["#A4D68C", "#87D3F2", "#A4C639", "#74BCEF", "#F2D387"]

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(8, 8))

# Dibujar un gráfico circular
porciones, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.1f%%', 
    startangle=140, colors=colores, 
    textprops={'color': 'black'}
)

# Embellir el texto de anotación (ajustar el tamaño, etc.)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

# Establecer el título
ax.set_title("Cambios en el presupuesto de los clientes para capacitación corporativa en 2022", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()