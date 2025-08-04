import matplotlib.pyplot as plt
import numpy as np

# Direcciones de mejora
direcciones = ["Enriquecer la variedad de audiolibros", "Mejorar la calidad del contenido", "Resolver el problema de homogeneización del contenido", 
              "Optimizar la recomendación personalizada", "Agregar funciones de interacción en comunidad", "Utilizar algoritmos de recomendación más precisos", "Crear una mejor interfaz de usuario"]
# Proporciones correspondientes (%)
proporciones = [38.16, 38.16, 35.37, 32.71, 32.31, 32.18, 32.05]

x = np.arange(len(direcciones))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(direcciones, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Direcciones de mejora de las plataformas de audiolibros chinas según los usuarios de audiolibros chinos en 2025')

plt.tight_layout()
plt.show()