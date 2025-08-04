import matplotlib.pyplot as plt
import numpy as np

# Nombres de las provincias
provincias = ["Guangdong", "Shandong", "Jiangsu", "Henan", "Zhejiang", "Beijing", "Hubei", "Hebei", "Hunan", "Sichuan"]
# Datos de índice de búsqueda simulados (se pueden reemplazar con datos reales), la longitud de los valores es consistente con el número de provincias
indice_busqueda = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9]  

y_pos = np.arange(len(provincias))

fig, ax = plt.subplots()
# Dibujar un gráfico de barras horizontales, height controla la altura de la barra (aquí simulada por el índice de búsqueda), width controla el ancho de la barra, align ajusta la alineación
ax.barh(y_pos, indice_busqueda, height=0.6, align='center', color='orange')  
ax.set_yticks(y_pos)
ax.set_yticklabels(provincias)
# Hacer que el gráfico de barras se muestre de izquierda a derecha (por defecto, el gráfico de barras horizontal es de abajo hacia arriba, después de invertir, se ajusta mejor a la vista del gráfico original)
ax.invert_yaxis()  
ax.set_xlabel('Esquema del Índice de Búsqueda')
ax.set_title('Resumen del Índice de Búsqueda')

# Puedes agregar etiquetas numéricas para mostrar los valores al final de cada barra
for i, v in enumerate(indice_busqueda):
    ax.text(v + 0.1, i, str(v), va='center')

plt.show()