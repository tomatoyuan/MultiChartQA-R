import matplotlib.pyplot as plt
import numpy as np

# Nombres de los escenarios
escenarios = [
    "Comprar para aliviar la sed", "Reunión social", "Trabajo en la oficina", "Mantener la vigilia durante la noche", 
    "Recepción familiar", "Acompañamiento de la comida diaria", "Horas extras nocturnas", "Entretenimiento empresarial", 
    "Viajes de negocios", "Regalos durante las fiestas", "Seguir la moda y experimentar"
]

# Datos de porcentaje correspondientes a cada escenario
porcentajes = [51, 47, 46, 46, 41, 38, 33, 23, 23, 22, 13]

# Ordenamiento de los datos (opcional)
ordenar_datos = True
if ordenar_datos:
    # Ordenar por porcentaje en orden descendente
    datos_ordenados = sorted(zip(porcentajes, escenarios), reverse=True)
    porcentajes, escenarios = zip(*datos_ordenados)

# Crear un lienzo y un subgráfico, establecer el tamaño del gráfico
fig, ax = plt.subplots(figsize=(12, 7))

# Utilizar colores degradados para rellenar el gráfico de barras
cmap = plt.cm.Greens
norm = plt.Normalize(min(porcentajes), max(porcentajes))
colores = cmap(norm(porcentajes))

# Crear un gráfico de barras
barras = ax.bar(escenarios, porcentajes, color=colores, edgecolor='black', linewidth=0.5)

# Agregar título y etiquetas
ax.set_title("Encuesta sobre los escenarios de consumo diario de té de los consumidores", fontsize=16, pad=20)
ax.set_ylabel("Porcentaje (%)", fontsize=12, labelpad=10)

# Establecer el ángulo de rotación y el tamaño de fuente de las etiquetas del eje x
plt.xticks(rotation=30, ha='right', fontsize=10)

# Agregar líneas de cuadrícula
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Agregar etiquetas numéricas encima de cada barra
for barra, porcentaje in zip(barras, porcentajes):
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width()/2.,
        altura + 0.8,  # Ajustar la posición de la etiqueta
        f'{porcentaje}%',
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

# Establecer el rango del eje y
plt.ylim(0, max(porcentajes) + 5)

# Agregar color de fondo
ax.set_facecolor('#f8f9fa')

# Optimizar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()