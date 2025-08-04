import matplotlib.pyplot as plt
import numpy as np

# Categorías de productos
etiquetas = ["Muebles de hogar duros", "Muebles de hogar suaves", "No compró y no entiende"]
# Proporciones correspondientes (%)
proporciones = [72.34, 67.53, 6.23]

# Configuración de ángulos para el gráfico de radar
num_vars = len(etiquetas)
angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Cerrar el gráfico de radar
proporciones_completas = proporciones + proporciones[:1]
angulos_completos = angulos + angulos[:1]

# Crear la figura con tamaño aumentado
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Dibujar el gráfico de radar
ax.fill(angulos_completos, proporciones_completas, color='orange', alpha=0.25)
ax.plot(angulos_completos, proporciones_completas, color='orange', linewidth=2)

# Agregar etiquetas de datos con posicionamiento optimizado
for i in range(num_vars):
    angulo = angulos[i]
    valor = proporciones[i]

    # Ajustar la posición de la etiqueta según el ángulo para evitar superposiciones
    if angulo == 0:
        ha = 'center'
        va = 'bottom'
        desplazamiento = 5
    elif angulo == np.pi/2:
        ha = 'left'
        va = 'center'
        desplazamiento = 5
    elif angulo == np.pi:
        ha = 'center'
        va = 'top'
        desplazamiento = -5
    elif angulo == 3*np.pi/2:
        ha = 'right'
        va = 'center'
        desplazamiento = -5
    elif 0 < angulo < np.pi/2:
        ha = 'left'
        va = 'bottom'
        desplazamiento = 5
    elif np.pi/2 < angulo < np.pi:
        ha = 'left'
        va = 'top'
        desplazamiento = 5
    elif np.pi < angulo < 3*np.pi/2:
        ha = 'right'
        va = 'top'
        desplazamiento = -5
    else:
        ha = 'right'
        va = 'bottom'
        desplazamiento = -5

    # Agregar la etiqueta con los parámetros de posición calculados
    ax.text(angulo, valor + desplazamiento, f'{valor}%', ha=ha, va=va, fontsize=12)

# Establecer límites y marcas del eje para evitar superposición de datos
ax.set_ylim(0, 85)
ax.set_yticks(np.arange(0, 85, 15))  # Ajustar intervalos de las marcas
ax.set_yticklabels([])  # Ocultar las etiquetas de marca predeterminadas

# Establecer etiquetas del eje
ax.set_xticks(angulos)
ax.set_xticklabels(etiquetas, fontsize=12)

# Establecer título
ax.set_title('Tipos de muebles de hogar comprados o conocidos por los consumidores chinos en 2025', fontsize=16, pad=20)

# Agregar leyenda y líneas de cuadrícula
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()