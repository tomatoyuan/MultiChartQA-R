import matplotlib.pyplot as plt
import numpy as np

# Nodos de tiempo
años = ["2018.12", "2019.6", "2020.3", "2020.6", "2020.12"]
# Número de usuarios de audio - visual en línea (en cientos de millones)
escala_usuarios = [7.32, 7.8, 8.57, 9.01, 9.44]
# Tasa de uso de usuarios de Internet (%)
tasa_uso = [88.3, 91.3, 94.8, 95.8, 95.4]

# Crear un lienzo y subgráficos con un eje y doble
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()

ax1.set_ylim(0, 20)  # Eje y para el número de usuarios (en cientos de millones)
ax2.set_ylim(75, 100)  # Eje y para la tasa de uso (%)

# Dibujar un gráfico de barras del número de usuarios de audio - visual en línea
x = np.arange(len(años))
ancho_barra = 0.6
barras = ax1.bar(x, escala_usuarios, width=ancho_barra, color="#A4C639", label="Número de usuarios de audio - visual en línea (en cientos de millones)")

# Dibujar un gráfico de línea de la tasa de uso de usuarios de Internet
linea, = ax2.plot(x, tasa_uso, marker='o', color="#64B5F6", label="Tasa de uso de usuarios de Internet (%)", linewidth=2)

# Agregar etiquetas de datos para el número de usuarios
for barra in barras:
    altura = barra.get_height()
    ax1.annotate(f'{altura}',
                 xy=(barra.get_x() + barra.get_width() / 2, altura),
                 xytext=(0, 3),  # Ajustar la posición de la etiqueta
                 textcoords="offset points",
                 ha='center', va='bottom')

# Agregar etiquetas de datos para la tasa de uso
for x_val, y_val in zip(x, tasa_uso):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),  # Ajustar la posición de la etiqueta
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#64B5F6")

# Establecer las marcas y etiquetas del eje x
ax1.set_xticks(x)
ax1.set_xticklabels(años)
# Establecer las etiquetas del eje y
ax1.set_ylabel("Número de usuarios de audio - visual en línea (en cientos de millones)", color="#A4C639", fontsize=10)
ax2.set_ylabel("Tasa de uso de usuarios de Internet (%)", color="#64B5F6")
# Establecer el título
ax1.set_title("Escala y uso de usuarios de audio - visual en línea en China de 2018 a 2020", fontsize=14, fontweight="bold")

# Combinar leyendas
handles, labels = ax1.get_legend_handles_labels()
handles.append(linea)
labels.append(linea.get_label())
ax1.legend(handles, labels, loc='upper left')

# Embelezar el gráfico ocultando los bordes superior y derecho (para ax1 y ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()