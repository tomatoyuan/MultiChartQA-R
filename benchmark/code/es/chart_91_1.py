import matplotlib.pyplot as plt

# Datos
etiquetas = ["China", "Europa", "América del Norte", "Japón", "Otros"]
tamaños = [65, 9, 8, 7, 10]
# Configuración de colores, lo más cercano posible a la imagen original
colores = ["#A4C639", "#8EBF8F", "#87CEEB", "#ADD8E6", "#FFD700"]  

# Crear un lienzo
fig, ax = plt.subplots(figsize=(6, 5))

# Dibujar un gráfico de pastel
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct="%1.1f%%",  
    startangle=90,     
    colors=colores,
    textprops={"color": "black"}
)

# Establecer el título, simular el título de fondo verde superior (implementado con un título normal + ajuste de posición)
ax.set_title("Participación en la producción mundial de termos de acero inoxidable", fontsize=14, fontweight="bold", y=1.08, backgroundcolor="#8EBF8F", pad=8)

# Embelezar: mantener el gráfico de pastel circular
ax.axis("equal")

plt.tight_layout()
plt.show()