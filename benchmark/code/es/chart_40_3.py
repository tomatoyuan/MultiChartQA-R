import matplotlib.pyplot as plt
import pandas as pd

# Construir datos
data = {
    'Canal': ['En línea (Plataforma de compras en línea)', 'En línea (Directo de Douyin)', 'Fuera de línea (Supermercado)', 'Fuera de línea (Tienda de conveniencia)', 'Fuera de línea (Pinduoduo)', 'Fuera de línea (Comedor)'],
    'Proporción': [89, 68, 74, 64, 57, 40]
}
df = pd.DataFrame(data)

# Crear un lienzo
plt.figure(figsize=(12, 6))

# Dibujar un gráfico de barras
colores = ['#4285F4', '#4285F4', '#EA4335', '#EA4335', '#EA4335', '#EA4335']  # Distinguir entre en línea (azul) y fuera de línea (rojo)
barras = plt.bar(df['Canal'], df['Proporción'], color=colores, alpha=0.8)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
             f'{altura}',
             ha='center', va='bottom', fontsize=10)

# Establecer título y etiquetas
plt.title('Distribución de la proporción de canales', fontsize=15)
plt.xlabel('Tipo de canal', fontsize=12)
plt.ylabel('Proporción', fontsize=12)

# Establecer el rango del eje y
plt.ylim(0, 100)

# Rotar las etiquetas del eje x para una mejor visualización
plt.xticks(rotation=45, ha='right')

# Agregar líneas de cuadrícula
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar leyenda
from matplotlib.patches import Patch
elementos_leyenda = [Patch(facecolor='#4285F4', label='En línea'),
                     Patch(facecolor='#EA4335', label='Fuera de línea')]
plt.legend(handles=elementos_leyenda, loc='upper right')

# Optimizar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()