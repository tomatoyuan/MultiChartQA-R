import matplotlib.pyplot as plt

# Datos de la proporción de edad (estimados)
etiquetas_edad = ['18-24', '25-29', '30-34', '35-39', '40+']
proporciones_edad = [25, 25, 20, 15, 15]

# Datos de la tasa de crecimiento interanual (estimados)
tasas_crecimiento = [80, 10, 50, 85, 70]  # Estimación de la altura de las barras que representan la tasa de crecimiento

# Establecer el estilo del gráfico
colores = ['#FF4C88', '#FFA6C1', '#FDBACD', '#FECEDC', '#FEE5EA']

# Crear un gráfico de dos columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar un gráfico circular
ax1.pie(proporciones_edad, labels=etiquetas_edad, autopct='%1.1f%%', startangle=90, colors=colores)
ax1.set_title("Proporción de edad de las personas que regalan a sus parejas en 2023")
ax1.axis('equal')

# Dibujar un gráfico de barras
barras = ax2.bar(etiquetas_edad, tasas_crecimiento, color=colores)
ax2.set_title("Tasa de crecimiento interanual")
ax2.set_ylabel("Índice de crecimiento")
ax2.set_ylim(0, 100)

# Agregar etiquetas de valor
for barra in barras:
    altura = barra.get_height()
    ax2.text(barra.get_x() + barra.get_width() / 2, altura + 2, f'{altura}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()