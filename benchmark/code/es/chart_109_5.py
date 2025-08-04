import matplotlib.pyplot as plt
import numpy as np

# Medidas de promoción
medidas = ["Presentar nuevos talentos jóvenes", "Fortalecer la construcción de infraestructura de red rural", "Apoyo político y financiero de los departamentos gubernamentales", 
            "Proporcionar instalaciones de alta calidad para la operación del comercio electrónico", "Fortalecer la capacitación de personal técnico y de gestión", "Apoyar a las empresas agrícolas para que ofrezcan más productos", 
            "Regular el mercado de comercio electrónico y crear un buen entorno empresarial", "Las asociaciones industriales brindan más orientación e información"]
# Proporción correspondiente (%)
proporciones = [28.79, 30.30, 30.45, 31.52, 31.67, 33.18, 34.09, 34.24]

y = np.arange(len(medidas))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 7))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(medidas)
ax.set_xlabel('Proporción (%)')
ax.set_title('Medidas consideradas efectivas para promover el desarrollo del comercio electrónico rural por los consumidores de comercio electrónico rural chinos en 2025')

plt.tight_layout()
plt.show()