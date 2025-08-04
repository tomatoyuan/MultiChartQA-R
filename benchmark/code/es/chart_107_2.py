import matplotlib.pyplot as plt
import numpy as np

# Factores de consideración
factores = ["Evaluación de otros", "Plan familiar compartido", "Precio", "Calidad del servicio al cliente", "Protección de privacidad y seguridad", "Calidad de la llamada", 
           "Tipos y cantidades de paquetes disponibles", "Cobertura de red", "Señal y velocidad de red", "Servicios adicionales (Números cortos, membresías de video, banda ancha, etc.)", 
           "Políticas de tráfico de datos (Transferencia de datos no utilizados, transferencia de datos, etc.)"]
# Proporciones correspondientes (%)
proporciones = [17.88, 21.73, 24.84, 26.45, 26.87, 27.41, 
               29.34, 30.73, 32.66, 32.87, 34.26]

y = np.arange(len(factores))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 7))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(factores)
ax.set_xlabel('Proporción (%)')
ax.set_title('Principales factores considerados por los usuarios chinos al elegir un operador telefónico en 2025')

plt.tight_layout()
plt.show()