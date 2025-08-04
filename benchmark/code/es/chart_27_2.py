import matplotlib.pyplot as plt

# Datos de fechas
fechas = ["28 de marzo", "30 de marzo", "1 de abril", "3 de abril", "5 de abril", "7 de abril", "9 de abril"]
# Datos numéricos correspondientes
valores = [290000, 290000, 580000, 870000, 1160000, 1450000, 1740000]

# Crear el lienzo y el subgráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de líneas, marker='o' muestra puntos, linewidth=2.5 engrosa las líneas
ax.plot(fechas, valores, color='red', marker='o', linewidth=2.5)  

# Configurar las divisiones y etiquetas del eje y
ax.set_yticks([290000, 580000, 870000, 1160000, 1450000, 1740000, 2030000])
ax.set_yticklabels(["290 mil", "580 mil", "870 mil", "1.16 millones", "1.45 millones", "1.74 millones", "2.03 millones"])

# Configurar las etiquetas del eje x, giradas 30 grados para mayor estética
ax.set_xticklabels(fechas, rotation=30, ha='right', fontsize=10)  

# Agregar líneas de cuadrícula para mejorar la legibilidad
ax.grid(True, linestyle='--', alpha=0.7)

# Agregar título y etiquetas de los ejes
plt.title("Tendencia del índice de búsqueda en línea de 'In the Name of the People'", fontsize=15, pad=20)
plt.xlabel("Fecha", fontsize=12)
plt.ylabel("Índice de búsqueda", fontsize=12)

# Emprolijar el borde del gráfico
for spine in ax.spines.values():
    spine.set_color('gray')

# Agregar etiquetas de datos
for x, y in zip(fechas, valores):
    ax.annotate(f'{y:,}', (x, y), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=9)

# Mostrar la gráfica
plt.tight_layout()
plt.show()