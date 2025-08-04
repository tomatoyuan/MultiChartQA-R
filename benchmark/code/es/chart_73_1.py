import matplotlib.pyplot as plt

# Datos
etiquetas = ["$10 - $20", "$21 - $30", "$31 - $40", "$41 o más"]
datos = [18.4, 50.3, 26.5, 4.8]
colores = ['#FFA07A', '#FF4500', '#FF8C00', '#FFD700']  # Tonos de colores cálidos

# Dibujar un gráfico de dona
fig, ax = plt.subplots(figsize=(8, 8))
porciones, textos, textos_automaticos = ax.pie(
    datos,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    wedgeprops=dict(width=0.4, edgecolor='white')  # Controlar el ancho para formar una dona
)

# Establecer el título
ax.set_title("Tarifas de pago único de las plataformas de entrega inmediata más utilizadas por los usuarios", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.show()