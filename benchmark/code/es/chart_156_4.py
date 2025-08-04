import matplotlib.pyplot as plt

# Definición de datos (posiciones más precisas, parecidas a la imagen original)
etiquetas = ['Sensación en la piel', 'Realismo', 'Invisibilidad', 'Naturalidad', 'Sensación de desnudo']
x_porcentaje_ventas = [0.05, 0.03, 0.04, 0.55, 0.75]  # Porcentaje de ventas
y_tasa_crecimiento = [2.8, 0.05, -0.02, 0.1, 0.12]   # Tasa de crecimiento año con año
tamaños = [500, 320, 300, 350, 360]  # Tamaño de las burbujas, establecido manualmente para acercarse al peso visual de la imagen original

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de burbujas
ax.scatter(
    x_porcentaje_ventas,
    y_tasa_crecimiento,
    s=tamaños,
    c='#FF8888',
    alpha=0.75,
    edgecolors='white',
    linewidth=1.5
)

# Agregar etiquetas de texto
for i in range(len(etiquetas)):
    ax.text(x_porcentaje_ventas[i], y_tasa_crecimiento[i] + 0.03, etiquetas[i],
            ha='center', va='bottom', fontsize=12)

# Configuración de los ejes
ax.set_title('Segmentación de puntos fuertes de funcionalidad de los \n'
             '"calcetines imitación piernas desnudas" en línea en Taobao en MAT2024\n'
             'Relacionado con la naturalidad del color', fontsize=15, weight='bold')
ax.set_xlabel('Porcentaje de ventas', fontsize=12)
ax.set_ylabel('Año con año', fontsize=12)

# Configurar el formato y el rango de las divisiones
ax.set_xlim(0, 0.9)
ax.set_ylim(-0.3, 3.2)
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
ax.set_xticklabels(['0%', '20%', '40%', '60%', '80%'])
ax.set_yticks([-1, 0, 1, 2, 3])
ax.set_yticklabels(['-100%', '0%', '100%', '200%', '300%'])

# Agregar cuadrícula y fondo
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_facecolor('#fcfcfc')

# Indicación de la fuente de los datos
texto_fuente = "Fuente de datos: Datos de Magic Mirror Market Intelligence; MAT2024: 2023.07 - 2024.06"
plt.figtext(0.5, -0.05, texto_fuente, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()