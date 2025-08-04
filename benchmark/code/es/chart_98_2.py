import matplotlib.pyplot as plt

# Datos de año y proporción
años = ["2020", "2021"]
porcentajes = [10, 13]
# Colores personalizados (ajustables)
colores = ["#A4C639", "#87CEEB"]

# Crear un lienzo (diseño de dos filas)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))  # Aumentar el tamaño del lienzo

# Establecer el título general
fig.suptitle("Proporción de transacciones en línea de vehículos eléctricos de litio de dos ruedas", fontsize=16, fontweight="bold", y=0.95)

# Dibujar el gráfico circular para 2020
wedges, texts, autotexts = ax1.pie(
    [porcentajes[0], 100 - porcentajes[0]],  # Mostrar la parte de la proporción y la parte restante
    labels=[años[0], ""],  # La etiqueta principal muestra el año
    colors=[colores[0], 'lightgray'],  # Usar el color principal para la parte de la proporción y gris claro para la parte restante
    autopct=lambda p: f'≈{p:.0f}%' if p >= porcentajes[0] else '',  # Mostrar solo el porcentaje en la parte de la proporción
    startangle=90,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}  # Agregar un borde blanco para la separación
)
ax1.set_title(f"Participación en el mercado en {años[0]}: {porcentajes[0]}%", fontsize=14, pad=10)  # Etiquetar claramente el año y la proporción
ax1.set_aspect('equal')  # Asegurar una forma circular

# Dibujar el gráfico circular para 2021
wedges, texts, autotexts = ax2.pie(
    [porcentajes[1], 100 - porcentajes[1]],
    labels=[años[1], ""],
    colors=[colores[1], 'lightgray'],
    autopct=lambda p: f'≈{p:.0f}%' if p >= porcentajes[1] else '',
    startangle=90,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)
ax2.set_title(f"Participación en el mercado en {años[1]}: {porcentajes[1]}%", fontsize=14, pad=10)
ax2.set_aspect('equal')

# Ocultar los bordes
for ax in [ax1, ax2]:
    ax.axis('off')  # Ocultar completamente los ejes

# Ajustar el espaciado entre subgráficos
plt.subplots_adjust(hspace=0.3)

plt.show()