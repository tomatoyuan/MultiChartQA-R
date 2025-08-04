import matplotlib.pyplot as plt

# Datos
etiquetas = ['Materiales Primarios de Biotecnología', 'Marcas de Belleza y Cuidado de la Piel', 'Tecnología Médica', 'Otros']
tamaños = [42, 25, 20, 13]  # Los valores aquí son simulados. Puedes reemplazarlos con datos reales, asegurándote de que la suma sea 100.
colores = ['#d9b3b3', '#f2d9a6', '#c7e0c3', '#d9d9d9']  # Colores personalizados

# Dibujar un gráfico de pastel
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
ax.set_title('Distribución de Empresas de Inversión y Financiamiento en Belleza Doméstica en 2024')

plt.show()