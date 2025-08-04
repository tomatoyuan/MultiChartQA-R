import matplotlib.pyplot as plt
import numpy as np

# Tipos de regalos
regalos = ["Teléfono móvil", "Chocolate", "Equipaje", "Flores", "Perfume"]
# Valores correspondientes de los regalos
valores = [430998, 416132, 411167, 323635, 124097]

# Crear un gráfico de barras horizontales
plt.figure(figsize=(10, 6))

# Definir colores personalizados
colores = ['#FF69B4', '#FF7F50', '#FFB6C1', '#FF1493', '#DB7093']

# Trazar las barras con colores personalizados
barras = plt.barh(regalos, valores, color=colores)

# Agregar título y etiquetas
plt.title('Ranking de regalos de San Valentín este año', fontsize=16)
plt.xlabel('Número de regalos', fontsize=12)
plt.ylabel('Tipo de regalo', fontsize=12)

# Agregar etiquetas de datos con números formateados
for barra in barras:
    ancho = barra.get_width()
    plt.text(ancho + 5000, barra.get_y() + barra.get_height()/2,
             f'{ancho:,}', ha='left', va='center', fontsize=10)

# Formatear las etiquetas del eje x con separador de miles
plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Agregar líneas de cuadrícula para mayor legibilidad
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Ajustar el diseño para evitar que se recorten las etiquetas
plt.tight_layout()

# Mostrar el gráfico
plt.show()