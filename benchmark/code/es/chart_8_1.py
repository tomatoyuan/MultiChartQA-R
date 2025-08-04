import matplotlib.pyplot as plt
import numpy as np

# Datos de fechas, representados por cadenas para posterior procesamiento de visualización
fechas = [f"Mayo {i}" for i in range(1, 32)]
# Datos aproximados de atención de búsqueda diaria (leídos del gráfico, solo un ejemplo, ajustar según la situación real)
valores = [60000, 57000, 62000, 80000, 100000, 90000, 95000, 90000, 80000, 70000, 
          65000, 45000, 60000, 58000, 55000, 48000, 52000, 50000, 47000, 55000, 
          70000, 55000, 65000, 70000, 75000, 78000, 78000, 78000, 80000, 82000, 85000]

# Establece las posiciones del eje x
x = np.arange(len(fechas))  

fig, ax = plt.subplots(figsize=(14, 7))  # Ajusta el tamaño del gráfico
# Dibuja un gráfico de línea y agrega puntos marcadores
line, = ax.plot(x, valores, color='blue', marker='o', markersize=4)  

# Establece las etiquetas del eje x, muestra cada tres días
indices_etiquetas_x = np.arange(0, len(fechas), 3)  # Toma índices cada 3 pasos
etiquetas_x = [fechas[i] for i in indices_etiquetas_x]
ax.set_xticks(indices_etiquetas_x)
ax.set_xticklabels(etiquetas_x)  

# Agrega anotaciones de datos
for i, (fecha, valor) in enumerate(zip(fechas, valores)):
    # Para los primeros 10 puntos de datos, anota arriba; para los siguientes 10, anota abajo para evitar salir del gráfico
    if i < 10:
        ax.annotate(f'{valor:,}',
                    xy=(i, valor),
                    xytext=(0, 10),  # Desplazamiento vertical de 10 puntos
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    rotation=0,
                    fontsize=8)
    elif i < 20:
        ax.annotate(f'{valor:,}',
                    xy=(i, valor),
                    xytext=(0, -10),  # Desplazamiento vertical de 10 puntos
                    textcoords="offset points",
                    ha='center',
                    va='top',
                    rotation=0,
                    fontsize=8)
    else:
        ax.annotate(f'{valor:,}',
                    xy=(i, valor),
                    xytext=(0, 10),  # Desplazamiento vertical de 10 puntos
                    textcoords="offset points",
                    ha='center',
                    va='bottom',
                    rotation=0,
                    fontsize=8)

# Establece títulos de ejes, etc.
ax.set_xlabel('Fecha', fontsize=12)
ax.set_ylabel('Atención de Búsqueda', fontsize=12)
ax.set_title('Tendencia de Atención de Búsqueda de la Industria de Litigios de Divorcio en Mayo', fontsize=14)

# Agrega líneas de cuadrícula
ax.grid(True, linestyle='--', alpha=0.7)

# Ajusta el rango del eje Y para dejar espacio para las anotaciones
y_min, y_max = ax.get_ylim()
ax.set_ylim(y_min - 5000, y_max + 5000)

plt.tight_layout()  # Asegura que todos los elementos quepan dentro del área del gráfico
plt.show()