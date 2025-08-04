import matplotlib.pyplot as plt

# Datos
canales = ['En línea', 'Tanto en línea como fuera de línea', 'Fuera de línea']
porcentajes = [89, 68, 74]

# Crear un lienzo
plt.figure(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = plt.bar(canales, porcentajes, color=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.8)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
             f'{altura}%',
             ha='center', va='bottom', fontsize=12)

# Establecer título y etiquetas
plt.title('Porcentaje de consumidores que incluyen canales en las decisiones de compra', fontsize=15)
plt.xlabel('Tipo de canal', fontsize=12)
plt.ylabel('Porcentaje (%)', fontsize=12)

# Establecer el rango del eje y
plt.ylim(0, 100)

# Agregar líneas de cuadrícula
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Optimizar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()