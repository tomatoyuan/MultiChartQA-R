import matplotlib.pyplot as plt
import numpy as np

# Requisitos de funciones de humanos digitales de IA
funciones = [
    "Reconocimiento de emociones", "Diálogo de múltiples rondas", "Capacidad de codificación", "Comunicación interlingüe (Traducción, etc.)", "Reescritura de texto", 
    "Lógica y razonamiento", "Reconocimiento de movimiento corporal", "Clasificación de texto", "Aprendizaje y evolución autónomos", "Generación y creación", 
    "Reconocimiento facial", "Interacción humano - máquina", "Comprensión del lenguaje natural", "Habilidad multimodal (Procesamiento de texto, imagen, voz, video)"
]
# Proporciones correspondientes (%)
proporciones = [17.69, 17.95, 18.88, 19.02, 19.41, 
               19.68, 20.61, 21.41, 21.54, 22.34, 
               22.34, 24.87, 25.66, 32.98]

y = np.arange(len(funciones))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(12, 8))
# Dibujar un gráfico de barras horizontal
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas a la derecha de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(funciones)
ax.set_xlabel('Proporción (%)')
ax.set_title('Requisitos funcionales de las empresas chinas para los humanos digitales de IA en 2025')

plt.tight_layout()
plt.show()