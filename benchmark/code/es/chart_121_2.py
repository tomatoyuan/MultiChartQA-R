import matplotlib.pyplot as plt

# Categorías de la composición de ingresos
etiquetas = ["Institucional y Trading", "Gestión de Patrimonios", "Banca de Inversión", "Gestión de Inversiones", "Negocios Internacionales", "Otros"]
# Proporciones correspondientes (%)
tamaños = [41.31, 26.99, 9.73, 13.14, 5.99, 2.84]
# Colores correspondientes (tratar de coincidir con la imagen original, se pueden ajustar)
colores = ['#E4725F', '#F6C85F', '#81C784', '#94572E', '#C08B30', '#4F4F4F']

fig, ax = plt.subplots(figsize=(6, 6))
# Dibujar un gráfico circular, autopct controla el formato de visualización numérica, startangle establece el ángulo de inicio
wedges, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.2f%%', startangle=90)

# Ajustar el color del texto de las anotaciones a blanco para que los valores sean más claros en los bloques de color
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white')

ax.set_title('Composición de Ingresos de Guotai Junan en 2023')

plt.tight_layout()
plt.show()