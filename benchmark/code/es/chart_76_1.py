import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["T1 2021", "T1 2022"]
tiempo_de_uso = [316.8, 332.9]
tasa_de_crecimiento = 5.1

# Colores: Contraste azul - naranja
colores = ['#6495ED', '#FFA07A']

# Configurar el lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# El eje y del gráfico de barras simétrico es el elemento compartido (aquí se establece como un solo elemento "Tiempo de uso diario de una sola máquina")
y = ["Tiempo de uso diario efectivo de una sola máquina"]
y_pos = np.arange(len(y))

# Longitudes de las barras horizontales (negativo para 2021, positivo para 2022)
barra_2021 = [-tiempo_de_uso[0]]
barra_2022 = [tiempo_de_uso[1]]

# Dibujar los gráficos de barras en los lados izquierdo y derecho
ax.barh(y_pos, barra_2021, color=colores[0], height=0.4, label=años[0])
ax.barh(y_pos, barra_2022, color=colores[1], height=0.4, label=años[1])

# Agregar etiquetas de datos
ax.text(barra_2021[0] - 10, y_pos[0], f"{tiempo_de_uso[0]}", va='center', ha='right', fontsize=10, color=colores[0])
ax.text(barra_2022[0] + 10, y_pos[0], f"{tiempo_de_uso[1]}", va='center', ha='left', fontsize=10, color=colores[1])

# Anotación de la tasa de crecimiento (flecha en el centro)
ax.annotate(f'+{tasa_de_crecimiento}%',
            xy=(0, y_pos[0]),
            xytext=(0, y_pos[0] + 0.3),
            ha='center',
            fontsize=11,
            color='green',
            arrowprops=dict(arrowstyle="->", color='green'))

# Configurar el eje x
ax.set_xticks(np.arange(-400, 401, 100))
ax.set_xlim(-400, 400)
ax.axvline(0, color='gray', linewidth=1)  # Línea central

# Configurar el eje y
ax.set_yticks(y_pos)
ax.set_yticklabels(y)
ax.set_title("mUserTracker: Comparación del tiempo de uso diario de una sola máquina entre el T1 2021 y el T1 2022 (Gráfico simétrico)", fontsize=13, fontweight="bold")

# Leyenda
ax.legend(loc='upper right')

# Mejora visual
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()