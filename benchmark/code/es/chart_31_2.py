import matplotlib.pyplot as plt

# Datos de la proporción de género
etiquetas = ["Mujer", "Hombre", "Otros (por ejemplo, rastreadores)"]
tamaños = [57, 40, 3]  # Ajustada la proporción de "Otros" para asegurar que la suma sea 100%
colores = ["#FFC0CB", "#87CEEB", "#D3D3D3"]  # Rosa (Mujer), Azul claro (Hombre), Gris claro (Otros)

# Crear un lienzo
plt.figure(figsize=(8, 8))

# Dibujar un gráfico de pastel
plt.pie(tamaños, 
        labels=etiquetas, 
        autopct='%1.1f%%',  # Mostrar porcentaje
        startangle=140,  # Ángulo de inicio
        colors=colores,
        explode=(0, 0, 0.1),  # Resaltar la categoría "Otros"
        shadow=True,  # Añadir sombra
        textprops={'fontsize': 12}  # Establecer tamaño de texto
       )

# Establecer el título y mostrar en proporción igual
plt.title("Proporción de Género de Usuarios de Búsqueda de Préstamos Universitarios", fontsize=16)
plt.axis('equal')  # Asegurar que el gráfico de pastel sea un círculo perfecto

# Mostrar el gráfico
plt.tight_layout()
plt.show()