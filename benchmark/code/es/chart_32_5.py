import matplotlib.pyplot as plt
import numpy as np

# Definir palabras clave y áreas correspondientes (decrecen en el orden especificado y se agrandan en general)
palabras_clave = ["Certificado de Calificación de Maestro", "Educación en Línea", "Plaza de Maestro", "Vacaciones de Maestro", "Beneficios de Maestro"]
tamaños = [152000, 111600, 9200, 6800, 4400]  # Duplicar el área en general
colores = ['#FFC2D1', '#BDE0FE', '#BDB2FF', '#A2D2FF', '#C8B6FF']  # Colores de las burbujas

# Crear un lienzo
plt.figure(figsize=(12, 10))  # Aumentar el tamaño del lienzo

# Generar posiciones uniformemente distribuidas (dispuestas en un círculo)
theta = np.linspace(0, 2*np.pi, len(palabras_clave), endpoint=False)
radio = 1.5  # Aumentar el radio del círculo para evitar la superposición de burbujas
x = radio * np.cos(theta)
y = radio * np.sin(theta)

# Dibujar un gráfico de burbujas
scatter = plt.scatter(x, y, s=tamaños, c=colores, alpha=0.7, edgecolors='w', linewidths=2)

# Agregar etiquetas
for i, txt in enumerate(palabras_clave):
    plt.annotate(txt, (x[i], y[i]), ha='center', va='center', 
                 fontsize=14, fontweight='bold', color='#333333')  # Aumentar el tamaño de la fuente

# Establecer propiedades del gráfico
plt.axis('equal')  # Asegurar que las burbujas sean circulares
plt.axis('off')    # Ocultar los ejes
plt.title("Gráfico de Burbujas de la Atención a Palabras Clave en la Industria de la Enseñanza", fontsize=18, pad=20)  # Aumentar el tamaño de la fuente del título

# Mostrar el gráfico
plt.tight_layout()
plt.show()