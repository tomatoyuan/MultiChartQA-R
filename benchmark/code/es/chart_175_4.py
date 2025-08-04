import matplotlib.pyplot as plt

# Datos
etiquetas = ['Salud médica', 'Tecnología de la información', 'Fabricación avanzada', 'Transporte automotriz', 'Nuevos consumos', 'Entretenimiento cultural', 'Fintech']
tamaños = [29.5, 25.1, 13.9, 11.7, 10.0, 9.6, 0.2]

# Crear la gráfica
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 10}
)
ax.axis('equal')

# Agregar título y fuente de los datos
plt.title('Distribución de industrias de empresas en el mercado internacional', fontsize=15, loc='center')
plt.figtext(0.01, 0, 'Fuente de datos: Bailian Intelligence, compilado por el Instituto de 36Kr',
            fontsize=10, ha='left')
plt.tight_layout()
plt.show()