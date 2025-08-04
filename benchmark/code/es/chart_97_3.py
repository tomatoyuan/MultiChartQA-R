import matplotlib.pyplot as plt

# Clasificación y proporción de años de ver partidos (datos simulados, similares a la imagen original)
etiquetas = ["Más de 5 años", "De 2 a 5 años", "Menos de 2 años"]
tamaños = [89.9, 7.6, 2.5]
# Combinación de colores libre (ajustable)
colores = ["#A4C639", "#87CEEB", "#FFD700"]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar un gráfico circular
porciones, textos, textos_automaticos = ax.pie(
    tamaños, 
    labels=etiquetas, 
    colors=colores, 
    autopct='%1.1f%%', 
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')  # Efecto de gráfico circular en forma de anillo (opcional, se puede eliminar para un gráfico circular sólido)
)

# Establecer el título
ax.set_title("Años de ver partidos de fútbol de los aficionados chinos al fútbol en 2022", fontsize=14, fontweight="bold", y=1.05)

# Embelezar las anotaciones (color, tamaño)
for texto, texto_automatico in zip(textos, textos_automaticos):
    texto.set_color('black')
    texto_automatico.set_color('black')
    texto_automatico.set_fontsize(10)

# Ocultar el borde (el gráfico circular no tiene borde real, solo para estandarizar el diseño)
for borde in ax.spines.values():
    borde.set_visible(False)

plt.tight_layout()
plt.show()