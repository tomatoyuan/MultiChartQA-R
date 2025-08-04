import matplotlib.pyplot as plt

# 数据
etiquetas = ['Aceptar los requisitos \nobligatorios de la política', 'Aceptar las razones de\n promoción de los valores \nambientales', 'Otros']
tamaños = [56.3, 37.4, 7.3]
colores = ['#058b83', '#abd7a6', '#efe9d2']  # Coincidir con los colores del gráfico

# Generar un gráfico circular
plt.figure(figsize=(8, 6))
segmentos, textos, textos_automaticos = plt.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    textprops={'fontsize': 14}
)

# Establecer el título
plt.title('Formas de promoción reconocidas por los consumidores', fontsize=16)

# Mostrar el gráfico
plt.tight_layout()
plt.show()