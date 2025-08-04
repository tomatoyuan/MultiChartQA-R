import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Datos
etiquetas = ["Deportes sobre hielo", "Actividades folclóricas de hielo y nieve", "Experiencias de observación de hielo y nieve", "Actividades terrestres de hielo y nieve"]
tamaños = [27, 37, 25, 11]
# Colores correspondientes (trata de coincidir con la imagen original y ajusta según la situación real)
colores = ['#4B9CD3', '#FF7F27', '#32CD32', '#FFD700']

fig, ax = plt.subplots(figsize=(8, 6))
# Dibuja un gráfico de dona, wedgeprops establece el ancho de la dona
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.1f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Añade un símbolo personalizado "¥" en el centro de la dona para simular el efecto de la imagen original
circulo_centro = Circle((0, 0), 0.3, color='white')
ax.add_artist(circulo_centro)
ax.text(0, 0, '¥', ha='center', va='center', fontsize=40, color='orange')

# Ajusta el tamaño y el color del texto de la anotación (opcional) para que la anotación sea más clara
for texto in textos:
    texto.set_fontsize(12)
for texto_automatico in textos_automaticos:
    texto_automatico.set_fontsize(10)
    texto_automatico.set_color('black')  # Hace que los valores sean más claros en los bloques de color

ax.set_title('Proporción de consumo de diferentes deportes de hielo y nieve durante la temporada de hielo y nieve 2023 - 2024')

plt.tight_layout()
plt.show()