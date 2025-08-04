import matplotlib.pyplot as plt
import numpy as np

# Datos de años
años = np.arange(2017, 2030)
# Datos simulados del tamaño del mercado (la tendencia general es similar, los valores se pueden ajustar según la situación real)
tamaño_mercado = [120, 125, 130, 133, 136, 139, 142, 145, 147, 149, 151, 153, 155]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras
barras = ax.bar(años, tamaño_mercado, color='#6699cc', width=0.8)

# Agregar etiquetas numéricas encima de cada barra
for barra, valor in zip(barras, tamaño_mercado):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura + 0.5,
            f'{valor}', ha='center', va='bottom')

# Marcar la Tasa de Crecimiento Anual Compuesto (TCAC) para dos períodos, aquí se encuentra manualmente la posición para marcar y se ajustan las coordenadas según la situación real
ax.text(2019, 140, '2017 - 2023\nTCAC: 1.85%', ha='center')
ax.text(2026, 140, '2024 - 2029P\nTCAC: 1.31%', ha='center')

# Agregar una línea vertical para separar los dos períodos
ax.axvline(x=2024, color='gray', linestyle='--')

# Establecer las etiquetas de las marcas del eje x, agregar el identificador "P" a los años después de 2025
etiquetas_x = [str(año) if año < 2025 else f"{año}P" for año in años]
ax.set_xticks(años)
ax.set_xticklabels(etiquetas_x, rotation=45)

# Establecer el título del gráfico
ax.set_title('Tamaño del mercado de limpieza de ropa en China desde 2014 hasta 2029')

# Mostrar el gráfico
plt.tight_layout()  # Ajustar el diseño para evitar la superposición de etiquetas
plt.show()