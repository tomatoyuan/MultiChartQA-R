import matplotlib.pyplot as plt
import numpy as np

# Razones de compra
razones = ["Monitoreo de salud", "Diseño de producto exquisito y personalizado", "Registrar el estado de ejercicio", "Mostrar y demostrar estatus", "Verificar la ubicación de niños o ancianos", 
           "Conveniencia para la vida diaria (por ejemplo, enviar y recibir mensajes y llamadas)", "Simple preferencia personal"]
# Proporciones correspondientes (%)
proporciones = [45.48, 44.71, 43.44, 40.38, 25.35, 25.10, 19.11]

x = np.arange(len(razones))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(razones, rotation=15, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Razones por las que los consumidores chinos compran relojes inteligentes en 2025')

plt.tight_layout()
plt.show()