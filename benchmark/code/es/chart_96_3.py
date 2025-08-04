import matplotlib.pyplot as plt
import numpy as np

# Datos de puntos débiles en el espacio de MPV
puntos_debil_espacio = {
    "Espacio de maletero insuficiente cuando se usa la tercera fila": 30.0,
    "Acceso inconveniente a la tercera fila": 28.3,
    "Baja flexibilidad y baja tasa de utilización del espacio": 25.0,
    "Espacio reducido en la tercera fila": 23.8,
    "Espacio de almacenamiento irrazonable o de poca cantidad": 22.9,
    "Espacio de maletero insuficiente después de plegar la tercera fila": 20.8,
    "Espacio reducido en la primera fila": 16.3,
    "Espacio reducido en la segunda fila": 11.7
}
# Datos de puntos débiles en la comodidad de conducción de MPV
puntos_debil_comodidad = {
    "Los asientos de la tercera fila no tienen ventanas": 29.9,
    "Malos efectos de sonido": 27.7,
    "Pobre efecto de amortiguación": 26.4,
    "Pobre rendimiento de aislamiento térmico": 25.5,
    "Pobre efecto del aire acondicionado": 22.1,
    "Alto ruido dentro del automóvil": 21.6,
    "Inconveniente para subir y bajar del vehículo": 18.6,
    "Pobre comodidad de los asientos": 18.2
}

# Extraer etiquetas y valores
etiquetas_espacio = list(puntos_debil_espacio.keys())
valores_espacio = list(puntos_debil_espacio.values())
etiquetas_comodidad = list(puntos_debil_comodidad.keys())
valores_comodidad = list(puntos_debil_comodidad.values())

# Esquema de colores (combinar libremente y ajustar)
colores_barras = ["#A4C639", "#87CEEB", "#FFD700", "#FF69B4", 
                  "#90EE90", "#B0C4DE", "#FFA07A", "#D8BFD8"]

# Crear un lienzo con dos columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=False)

# Dibujar el gráfico de barras horizontales para los puntos débiles de espacio
x1 = np.arange(len(etiquetas_espacio))
ax1.barh(x1, valores_espacio, color=colores_barras, height=0.6)
ax1.set_yticks(x1)
ax1.set_yticklabels(etiquetas_espacio, fontsize=9)
ax1.set_title("MPV [Espacio] Puntos débiles\n(N = 240)", fontsize=12, fontweight="bold")
# Agregar anotaciones para los puntos débiles de espacio
for i, val in enumerate(valores_espacio):
    ax1.annotate(f'{val}%', (val + 1, i), va='center', fontsize=8)

# Dibujar el gráfico de barras horizontales para los puntos débiles de comodidad de conducción
x2 = np.arange(len(etiquetas_comodidad))
ax2.barh(x2, valores_comodidad, color=colores_barras, height=0.6)
ax2.set_yticks(x2)
ax2.set_yticklabels(etiquetas_comodidad, fontsize=9)
ax2.set_title("MPV [Comodidad de conducción] Puntos débiles\n(N = 231)", fontsize=12, fontweight="bold")
# Agregar anotaciones para los puntos débiles de comodidad de conducción
for i, val in enumerate(valores_comodidad):
    ax2.annotate(f'{val}%', (val + 1, i), va='center', fontsize=8)

# Embellir: Ocultar los bordes superior y derecho
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(axis='x', linestyle='--', alpha=0.3)  # Agregar cuadrícula auxiliar

plt.tight_layout()
plt.show()