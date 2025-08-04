import matplotlib.pyplot as plt

# Soporte para la visualización de caracteres chinos
plt.rcParams['font.sans-serif'] = ['SimHei']  # Utilizar la fuente Hei
plt.rcParams['axes.unicode_minus'] = False    # Resolver el problema de la visualización del signo menos

# Datos
etiquetas = [
    "Las funciones de la IA son\n cada vez más poderosas\n(42%)",
    "Uso moderado de la IA\n(23%)",
    "La IA debe complementarse\n con la educación familiar\n(22%)",
    "Actitud de duda hacia la IA\n(13%)"
]
tamaños = [42, 23, 22, 13]
colores = ['#FF0000', '#FF6666', '#FF9999', '#CCCCCC']

# Dibujar un gráfico circular anular
fig, ax = plt.subplots(figsize=(10, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.0f%%', startangle=90,
    colors=colores, wedgeprops=dict(width=0.4), textprops={'fontsize': 12}
)

# Añadir texto en el centro
plt.text(0, 0.1, "87%", fontsize=26, fontweight='bold', ha='center')
plt.text(0, -0.1, "de los padres tiene una\nactitud positiva hacia la IA", fontsize=14, ha='center')

# Establecer una relación de aspecto igual
ax.axis('equal')
plt.title("Actitudes de los padres hacia la educación basada en la IA", fontsize=16)
plt.tight_layout()
plt.show()