import matplotlib.pyplot as plt
import numpy as np

# Factores a considerar
factores = ["Origen", "Calidad", "Marca", "Empaque", "Precio", "Certificación Orgánica/Ecológica", 
            "Frescura", "Contenido Nutricional", "Conveniencia de Compra", "Reputación del Proveedor", "Servicio Posventa", "Promociones"]
# Proporciones correspondientes (%)
proporciones = [42.42, 38.64, 35.00, 33.64, 29.70, 28.79, 
                21.82, 21.36, 14.09, 13.33, 12.73, 6.67]

x = np.arange(len(factores))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(factores, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Factores Considerados por los Consumidores de Comercio Electrónico Rural Chino al Comprar Productos Agrícolas en 2025')

plt.tight_layout()
plt.show()