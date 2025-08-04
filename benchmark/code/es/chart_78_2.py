import matplotlib.pyplot as plt
import numpy as np

# Nombres de las regiones
regiones = ["Oceanía", "Europa", "Asia Oriental", "América Latina y el Caribe", "África subsahariana"]
# Tasa de matrícula en la escuela secundaria (%)
matricula_escuela_secundaria = [95.0, 93.6, 86.4, 78.7, 41.9]
# Tasa de participación en la educación profesional (%)
participacion_educacion_profesional = [17.5, 18.1, 7.2, 6.9, 1.3]
# PIB per cápita (USD)
pib_per_capita = [49999.0, 34148.9, 13463.6, 7244.7, 1501.2]

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 120)

# Dibujar un gráfico de barras agrupadas
x = np.arange(len(regiones))
ancho_barra = 0.35
# Tasa de matrícula en la escuela secundaria (verde)
barras_escuela_secundaria = ax.bar(x - ancho_barra/2, matricula_escuela_secundaria, width=ancho_barra, color="#A4C639", label="Tasa de matrícula en la escuela secundaria en cada región (%)")
# Tasa de participación en la educación profesional (azul)
barras_educacion_profesional = ax.bar(x + ancho_barra/2, participacion_educacion_profesional, width=ancho_barra, color="#64B5F6", label="Tasa de participación en la educación profesional de jóvenes de 15 - 24 años en cada región (%)")

# Agregar etiquetas de datos para la tasa de matrícula en la escuela secundaria
for bar in barras_escuela_secundaria:
    altura = bar.get_height()
    ax.annotate(f'{altura}%',
                xy=(bar.get_x() + bar.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar etiquetas de datos para la tasa de participación en la educación profesional
for bar in barras_educacion_profesional:
    altura = bar.get_height()
    ax.annotate(f'{altura}%',
                xy=(bar.get_x() + bar.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(regiones)
# Establecer la etiqueta del eje y
ax.set_ylabel("Porcentaje (%)")
# Establecer el título
ax.set_title("Tasa de participación en la educación profesional y tasa de matrícula en la escuela secundaria en cada región en 2020", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embelezar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()