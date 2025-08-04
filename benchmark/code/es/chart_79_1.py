import matplotlib.pyplot as plt

# Categorías
etiquetas = ["Mayor atención y confianza", "Otros"]
# Proporción de cada categoría (%), se aceptan datos aproximados
tamaños = [65.0, 35.0]
# Colores de cada parte del gráfico circular, tratar de acercarse a la imagen original
colores = ["#A4C639", "#64B5F6"]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar un gráfico circular
segmentos, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.1f%%', 
    startangle=90, colors=colores, 
    textprops={'color': 'black'}
)

# Embelezar el texto de anotación (ajustar el tamaño, etc.)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

# Agregar el texto explicativo inferior
ax.text(0.5, -0.2, "● El 65% de los consumidores indicó que su atención y confianza en la medicina tradicional china aumentó después de la pandemia.", 
        ha='center', va='bottom', fontsize=10, color='green')

# Establecer el título
ax.set_title("Atención y confianza en la medicina tradicional china para el diagnóstico y tratamiento de la COVID - 19 en 2021", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()