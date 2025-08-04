import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Lista de países
paises = ["China", "India", "Japón", "EE. UU.", "Brasil", "Turquía", "Tailandia", "Indonesia"]
# Datos del tamaño del mercado
tamano_mercado = [6, 1, 1, 1, 1, 0.5, 0.5, 0.5]

# Generar un arreglo de índices para los países
x = np.arange(len(paises))
# Crear un gráfico de barras con diferentes paletas de colores
sns.barplot(x=paises, y=tamano_mercado, palette=['orange'] + ['green']*(len(paises)-1))

# Agregar etiquetas de valor en las barras
for i, v in enumerate(tamano_mercado):
    plt.text(i, v + 0.05, f'{v}', ha='center', fontsize=12)

# Agregar texto especial en la primera barra
plt.text(0, tamano_mercado[0], "Más de seis veces", ha='center', va='bottom', fontsize=14, color='orange')
# Establecer el título del gráfico
plt.title("Tamaño estimado del mercado de té de los principales países en 2022", fontsize=14, fontweight='bold')
# Agregar texto en la parte inferior de la figura
plt.figtext(0.5, 0.01, "Unidad: Miles de millones de dólares estadounidenses", ha='center', fontsize=12)
# Remover las etiquetas de las marcas del eje y
plt.yticks([])
# Ajustar el diseño para evitar que el texto se obscurda
plt.tight_layout()
# Mostrar el gráfico
plt.show()