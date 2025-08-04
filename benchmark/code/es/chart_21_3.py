import matplotlib.pyplot as plt
import numpy as np

# Etiquetas de fechas
etiquetas = ["15 de la 12ª luna", "16 de la 12ª luna", "17 de la 12ª luna",
             "18 de la 12ª luna", "19 de la 12ª luna", "20 de la 12ª luna",
             "21 de la 12ª luna", "22 de la 12ª luna", "23 de la 12ª luna",
             "24 de la 12ª luna", "25 de la 12ª luna", "26 de la 12ª luna",
             "27 de la 12ª luna", "28 de la 12ª luna", "29 de la 12ª luna",
             "Nochevieja"]
# Datos simulados, generalmente mostrando una tendencia de picos, se pueden ajustar según la situación real
datos = [5, 8, 10, 7, 9, 11, 12, 13, 14, 18, 15, 16, 17, 20, 19, 6]
# Índices de las fechas pico (24 y 28 de la 12ª luna, correspondientes a los índices 9 y 13 en las etiquetas anteriores)
indices_pico = [9, 13]

x = np.arange(len(etiquetas))  # Posiciones del eje x
ancho = 0.6  # Ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))  # Crear un lienzo y ejes
# Dibujar el gráfico de barras, la mayoría de las barras de un color, las barras pico de otro color
barras = []
for i in range(len(x)):
    if i in indices_pico:
        barra = ax.bar(x[i], datos[i], ancho, color='#e65142')  # Color pico, similar al rojo en el gráfico original
    else:
        barra = ax.bar(x[i], datos[i], ancho, color='#80cbc4')  # Color de las otras barras, similar al cian - verde en el gráfico original
    barras.append(barra)

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=45, ha='right')

# Establecer el título
ax.set_title('Dos picos para la compra de boletos: 24 y 28 de la 12ª luna', fontsize=16, pad=20)

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Añadir algunos elementos decorativos, simulando el sol y las nubes en el gráfico original (simplemente indicados, se pueden refinar según los requisitos)
import matplotlib.patches as patches
# Dibujar un pequeño sol
sol = patches.Circle((1, max(datos) + 2), radius=1, color='yellow', alpha=0.8)
ax.add_patch(sol)
# Dibujar nubes (simuladas por rectángulos simples, se pueden dibujar con más precisión)
nube1 = patches.Rectangle((3, max(datos) + 1.5), 2, 1, color='white', alpha=0.8)
nube2 = patches.Rectangle((6, max(datos) + 1), 2, 1, color='white', alpha=0.8)
ax.add_patch(nube1)
ax.add_patch(nube2)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()