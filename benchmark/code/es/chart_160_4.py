import matplotlib.pyplot as plt

# 数据
etiquetas = ['Comercio electrónico', 'Electrónica y electrodomésticos', 'Juegos para móvil', 'Automóvil', 'Maquillaje']
tamaños = [45, 13.75, 13.75, 13.75, 13.75]  # La suma es 100
colores = ['#b3cfff', '#c2d6ff', '#d1ddff', '#e0e5ff', '#eff2ff']  # Degradado de azul más claro

# Dibujar el gráfico
fig, ax = plt.subplots()
segmentos, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=colores,
    textprops={'color': 'black', 'fontsize': 10}
)

# Agregar título
plt.title('Top 5 industrias de colaboración de los influencers de \n'
          'nivel intermedio de Bilibili en los últimos 180 días', fontsize=14)

# Agregar texto explicativo
plt.text(0, -1.3, "El número promedio de industrias de colaboración de los influencers\n"
                  " de nivel intermedio de Bilibili en los últimos 180 días es 2.77", ha='center', fontsize=12, color='#4a64c0')

# Mantener el gráfico circular
ax.axis('equal')

plt.tight_layout()
plt.show()