import matplotlib.pyplot as plt
import numpy as np

# Nombres de las etapas
etapas = ["Antes del embarazo", "Embarazo", "Crianza"]
# Categorías de información correspondientes a cada etapa (ordenadas según la leyenda, deben corresponder a los datos reales)
categorias = ["Conocimientos de preparación antes del embarazo", "Nutrición antes del embarazo", "Monitoreo antes del embarazo",
              "Mantenimiento del embarazo", "Ropa materna", "Registro del desarrollo fetal",
              "Recetas de dieta durante el embarazo", "Conocimientos de parto", "Ropa/productos para bebés",
              "Comida para bebés", "Productos/cursos de cuidado postparto"]
# Datos simulados (deben ser reemplazados con datos completos reales, aquí la sublista de cada etapa corresponde a la proporción en el orden de las categorías)
# En uso real, los valores de proporción de cada etapa y categoría deben ser llenados con precisión según el gráfico
datos = {
    "Antes del embarazo": [1.43, 15.89, 21.38, 23.63, 21.59, 21.18, 18.33, 16.09, 14.66, 8.76, 5.91],
    "Embarazo": [7.33, 12.22, 21.38, 31.77, 22.00, 23.83, 23.83, 15.89, 10.79, 6.52, 2.24],
    "Crianza": [4.48, 9.57, 15.27, 20.98, 20.98, 20.98, 17.92, 13.85, 18.33, 15.48, 8.15]
}
# Colores correspondientes (deben ser coincididos con precisión según la leyenda del gráfico, aquí es solo un ejemplo, lo real se basa en el gráfico)
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
           '#00BFFF', '#FFD700', '#1E90FF', '#FF69B4', '#00FA9A', '#FFA07A']

x = np.arange(len(etapas))  # El eje x corresponde a tres etapas
ancho_barra = 0.8  # Ancho de la barra

fig, ax = plt.subplots(figsize=(12, 8))
base = np.zeros(len(etapas))

for i, categoria in enumerate(categorias):
    # Recorrer cada categoría de información de interés y dibujar columnas apiladas
    ax.bar(etapas, [datos[etapa][i] for etapa in etapas], width=ancho_barra,
           bottom=base, color=colores[i], label=categoria)
    # Agregar anotaciones numéricas (solo un ejemplo, si hay muchos datos, pueden solaparse, y la posición, tamaño de fuente, etc. se pueden ajustar según sea necesario)
    for j in range(len(etapas)):
        ax.text(j, base[j] + datos[etapas[j]][i] / 2,
                f'{datos[etapas[j]][i]:.2f}', ha='center', va='center', fontsize=7)
    base += [datos[etapa][i] for etapa in etapas]

ax.set_ylabel('Proporción (%)')
ax.set_title('Información clave de interés de los consumidores de productos maternos y infantiles chinos en cada etapa en 2025')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Colocar la leyenda a la derecha para evitar la superposición
plt.xticks(x, etapas)
plt.tight_layout()
plt.show()