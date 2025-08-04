import matplotlib.pyplot as plt
import numpy as np

# Nombres de países/regiones
paises = ["EE. UU.", "China", "Japón", "Reino Unido", "Alemania", "India", "China [Economía de las Mujeres]", "Francia", "Italia", "Canadá", "Australia"]
# Datos correspondientes (Unidad: Trillones de yuanes, estimados aproximadamente según el gráfico aquí, puedes ajustarlos según los datos precisos reales)
datos = [1500, 600, 200, 200, 200, 200, 100, 100, 100, 100, 100]  

x = np.arange(len(paises))  # Posición en el eje x
ancho = 0.5  # Ancho de las barras

fig, ax = plt.subplots()

# Establecer colores para cada barra, "China [Economía de las Mujeres]" es naranja, el resto es cian
colores = ['cyan'] * len(paises)
indice = paises.index("China [Economía de las Mujeres]")
colores[indice] = 'orange'

rects = ax.bar(x, datos, ancho, color=colores)

# Corrección: Usar el parámetro bbox en lugar del parámetro de relleno y mover la anotación hacia arriba
ax.text(5.7, 300, "Más de 10 billones de yuanes", fontsize=12, ha='center', va='bottom',
        bbox=dict(facecolor='orange', alpha=1.0, pad=5))

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(paises, rotation=45, ha='right')
# Establecer la etiqueta del eje y
ax.set_ylabel('Escala (Trillones de yuanes)')
# Establecer el título
ax.set_title('En 2023, la escala de la "Economía de las Mujeres" en China es lo suficientemente grande como para formar la séptima economía más grande')

# Mostrar el gráfico
plt.tight_layout()
plt.show()