import matplotlib.pyplot as plt
# Datos
etiquetas = ["Gastar mucha energía y tiempo en buscar ingredientes saludables sin instrucciones claras en las etiquetas",
             "Preocuparse por los aditivos alimentarios excesivos",
             "Incapaz de juzgar si los alimentos instantáneos o las comidas entregadas a domicilio son saludables",
             "Dificultad para encontrar un canal de compra confiable a largo plazo",
             "Preocuparse por el contenido calórico de cada alimento y temer ganar peso"]
porcentajes = [60, 55, 47, 44, 18]

# Crear un objeto de trazado
fig, ax = plt.subplots()

# Dibujar un gráfico de barras horizontales
ax.barh(etiquetas, porcentajes, color='green')

# Agregar etiquetas de porcentaje
for i, v in enumerate(porcentajes):
    ax.text(v + 1, i, f'{v}%', va='center')

# Establecer el título y las etiquetas de los ejes (ajustar según sea necesario)
ax.set_title('Preocupaciones sobre ingredientes saludables')

# Mostrar el gráfico
plt.show()