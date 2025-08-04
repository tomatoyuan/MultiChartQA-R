import matplotlib.pyplot as plt

# 数据
etiquetas = ['No es necesario \nreemplazar diariamente', 'Es necesario \nreemplazar diariamente']
tamaños = [62.6, 37.4]
colores = ['#058b83', '#abd7a6']  # Usar la misma combinación de colores que el gráfico

# Generar el gráfico circular
plt.figure(figsize=(8, 6))
porciones, textos, textos_automaticos = plt.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    textprops={'fontsize': 14}
)

# Establecer el título
plt.title('Porcentaje de personas que no necesitan reemplazar diariamente\n los artículos de uso único en una estancia múltiple', fontsize=16)

# Mostrar el gráfico
plt.tight_layout()
plt.show()