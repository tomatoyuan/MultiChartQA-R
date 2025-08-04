import matplotlib.pyplot as plt

# Datos del gráfico circular
etiquetas = ['Entiende el significado \nde la insignia azul (50%)',
             'Ha oído hablar pero no conoce\n el significado específico (48%)',
             'No conoce en absoluto (4%)']
tamaños = [50, 48, 4]
colores = ['#4A90E2', '#50E3C2', '#B8E986']  # Colores personalizados

# Crear el gráfico circular
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    colors=colores,
    autopct='%1.0f%%',
    startangle=140,
    textprops={'fontsize': 10}
)

# Agregar título
plt.title('Distribución del conocimiento de los consumidores sobre la \ninsignia azul de los suplementos dietéticos', fontsize=14, fontweight='bold')

# Agregar fuente de datos
plt.figtext(0.5, 0.01, 'Fuente de datos: Datos de la encuesta de la población de canales integrales de suplementos \ndietéticos de CBNData en 2023',
            wrap=True, horizontalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()