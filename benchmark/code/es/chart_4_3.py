import matplotlib.pyplot as plt
import numpy as np

# Utiliza exactamente los datos que se proporcionaron
fechas = [f"5/{i}" for i in range(1, 32)]
valores = [
    7200000, 7000000, 7800000, 6800000, 6500000, 6800000, 7000000, 6200000, 
    6500000, 5800000, 7000000, 500000, 7200000, 3500000, 4000000, 3000000, 
    3500000, 4500000, 5200000, 4800000, 4500000, 4300000, 5000000, 5500000, 
    6000000, 6200000, 6800000, 6000000, 6500000, 7000000, 7500000
]

# Crea un lienzo
fig, ax = plt.subplots(figsize=(10, 5))  # Hace el lienzo un poco más ancho para acomodar más puntos de datos

# Dibuja un gráfico de línea con el mismo color y grosor de línea que la imagen original
ax.plot(fechas, valores, color="#4285f4", linewidth=2.5)

# Establece el título
ax.set_title("Tendencia de atención de noticias de la industria de estética médica en mayo", fontsize=14, fontweight="bold")

# Establece el eje y (Atención)
ax.set_ylabel("Atención", fontsize=12)
ax.set_ylim(0, 9000000)  # Coincide con el rango del eje y de la imagen original
ax.set_yticks(np.arange(0, 10000000, 1000000))  # El intervalo de las marcas del eje y es de 1 millón

# Establece el eje x (Fecha) - Muestra una marca cada 3 días
ax.set_xticks(np.arange(0, len(fechas), 3))  # Muestra una marca cada 3 días
ax.set_xticklabels([fechas[i] for i in range(0, len(fechas), 3)], rotation=45, ha="right")  # Rota 45 grados para evitar superposición

# Agrega líneas de cuadrícula
ax.grid(linestyle="--", color="gray", alpha=0.5)

# Optimiza el diseño
plt.tight_layout()

# Muestra el gráfico
plt.show()