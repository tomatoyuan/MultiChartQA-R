import matplotlib.pyplot as plt
import numpy as np

# Datos de fechas
fechas = ['1 de julio', '6 de julio', '11 de julio', '16 de julio', '21 de julio', '26 de julio']
# Datos de índice de búsqueda
indice_ insolación = [7000, 10000, 10000, 14000, 7000, 42000]
indice_enfermedad_aire_acondicionado = [3500, 7000, 7000, 10000, 10000, 21000]

# Convertir fechas a índices para la gráfica
x = np.arange(len(fechas))

# Crear un objeto de gráfica
fig, ax = plt.subplots(figsize=(12, 7))

# Establecer un fondo degradado (de azul claro a azul oscuro)
gradiente = np.linspace(0.95, 0.85, 256).reshape(256, 1)
ax.imshow(gradiente, aspect='auto', extent=[0, len(fechas)-1, 0, max(indice_ insolación)*1.1],
          alpha=0.3, cmap=plt.cm.Blues)

# Graficar el gráfico de líneas optimizado
ax.plot(x, indice_ insolación, color='#FF3333', marker='o', markersize=8,
        label='Insolación', linewidth=3, alpha=0.8)
ax.plot(x, indice_enfermedad_aire_acondicionado, color='#FF9933', marker='o', markersize=8,
        label='Enfermedad por Aire Acondicionado', linewidth=3, alpha=0.8)

# Establecer el eje x y el eje y
ax.set_xticks(x)
ax.set_xticklabels(fechas, fontsize=12)
ax.set_ylabel('Índice de Búsqueda', fontsize=14, labelpad=10)
ax.set_ylim(0, max(indice_ insolación) * 1.1)  # Dejar algo de espacio en la parte superior

# Establecer el título bonificado
ax.set_title('Tendencia de Comparación del Índice de Búsqueda entre Enfermedad por Aire Acondicionado e Insolación',
             fontsize=18, fontweight='bold', pad=20, color='#333333')

# Agregar etiquetas de datos
for i, (xi, yi) in enumerate(zip(x, indice_ insolación)):
    ax.annotate(f'{yi}', (xi, yi), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')

for i, (xi, yi) in enumerate(zip(x, indice_enfermedad_aire_acondicionado)):
    ax.annotate(f'{yi}', (xi, yi), textcoords='offset points',
                xytext=(0, -15), ha='center', fontsize=10, fontweight='bold')

# Agregar líneas de cuadrícula
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Establecer la leyenda y los bordes
ax.legend(fontsize=12, loc='upper left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#AAAAAA')
ax.spines['bottom'].set_color('#AAAAAA')

# Ajustar el diseño
plt.tight_layout()

# Mostrar la gráfica
plt.show()