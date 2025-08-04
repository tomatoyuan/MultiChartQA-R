import matplotlib.pyplot as plt

# Datos originales (utilizando directamente el número de asteriscos)
provincias = ["Guangdong", "Jiangsu", "Shandong", "Zhejiang", "Henan", "Taiwan", "Sichuan", "Hebei", "Hubei", "Hunan"]
estrellas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Número de asteriscos correspondiente a cada provincia

# Invertir el orden de los datos para que la provincia con la mayor calificación de estrellas esté en la parte superior
provincias_invertidas = provincias[::-1]
estrellas_invertidas = estrellas[::-1]

# Crear un lienzo
plt.figure(figsize=(12, 6))

# Dibujar un gráfico de barras horizontales (la provincia con la mayor calificación de estrellas está en la parte superior)
plt.barh(provincias_invertidas, estrellas_invertidas, color='skyblue')

# Agregar etiquetas de asteriscos
for i, (provincia, cantidad_estrellas) in enumerate(zip(provincias_invertidas, estrellas_invertidas)):
    plt.text(cantidad_estrellas + 0.2, i, '★' * cantidad_estrellas, va='center', fontsize=12)

# Establecer el título del gráfico y las etiquetas de los ejes
plt.title('Ranking del PIB de las provincias y ciudades chinas en 2015')
plt.xlabel('Número de estrellas')
plt.ylabel('Provincia')

# Establecer el rango del eje x
plt.xlim(0, max(estrellas_invertidas) + 2)  # Dejar suficiente espacio para mostrar los asteriscos

# Embelezar el gráfico
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()  # Asegurar un diseño compacto
plt.show()