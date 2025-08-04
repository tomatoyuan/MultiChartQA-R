import matplotlib.pyplot as plt

# Datos (valores hipotéticos de volumen de búsqueda, se pueden reemplazar con datos reales)
ciudades = ['Beijing', 'Shanghai', 'Chengdu']
volumenes_de_busqueda = [2200000, 950000, 780000]  # Valores hipotéticos de volumen de búsqueda

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))  # Establecer el tamaño del gráfico
barras = plt.bar(ciudades, volumenes_de_busqueda, color=['#b378d8', '#4b79e2', '#4b79e2'])

# Agregar título y etiquetas
plt.title('Comparación de los Volúmenes de Búsqueda del Certificado de Profesorado en Ciudades', fontsize=16, fontweight='bold')
plt.xlabel('Ciudades', fontsize=14)
plt.ylabel('Volumen de Búsqueda (veces)', fontsize=14)

# Agregar etiquetas numéricas
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura + 10000,
             f'{altura:,}', ha='center', va='bottom', fontsize=12)

# Establecer el formato de las marcas del eje y para que sea más legible
plt.ticklabel_format(axis='y', style='plain')

# Mostrar líneas de cuadrícula
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()  # Asegurarse de que las etiquetas y títulos se muestren completamente
plt.show()