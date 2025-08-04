import matplotlib.pyplot as plt
import numpy as np

# Aspectos de preocupación
aspectos = ["Precio", "Diseño y operación de la interfaz", "Batería", "Diseño de apariencia", "Velocidad de emparejamiento del teléfono", "Precisión de uso", 
            "Función a prueba de agua", "Servicio postventa", "Marca", "Función anti-roce"]
# Proporciones correspondientes (%)
proporciones = [47.77, 44.33, 40.38, 36.56, 33.63, 32.48, 
                22.93, 22.17, 21.91, 14.01]

x = np.arange(len(aspectos))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(aspectos, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Aspectos que preocupan a los consumidores chinos al comprar relojes inteligentes en 2025')

plt.tight_layout()
plt.show()