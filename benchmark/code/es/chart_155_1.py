import matplotlib.pyplot as plt

# 数据
etiquetas = ['Mercado de servicios médicos', 'Mercado de medicamentos', 'Mercado de productos no farmacéuticos', 'Mercado de servicios médicos de consumo', 'Infraestructura médica']
tamaños = [53.9, 19.6, 13.7, 9.8, 2.9]
colores = ['#a6d854', '#d9ef8b', '#ffffbf', '#fee08b', '#f46d43']

fig, ax = plt.subplots(figsize=(8, 6))

# Dibujo del gráfico circular
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    colors=colores,
    autopct='%.2f%%',
    startangle=90,
    textprops={'fontsize': 10},
    wedgeprops={'edgecolor': 'white'}
)

# Título
ax.set_title('Distribución de la cuota de mercado segmentada \nde la industria de la gran salud en China en 2022', fontsize=14, weight='bold', pad=20)

# Establece la relación de aspecto igual para que sea un círculo
ax.axis('equal')

plt.tight_layout()
plt.show()