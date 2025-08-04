import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Construir datos
provincias = ["Guangdong", "Zhejiang", "Beijing", "Guangxi", "Shandong", "Sichuan", "Fujian", "Shanghai", "Liaoning", "Otros"]
porcentajes = [16.3, 7.5, 6.2, 5.7, 5.7, 5.6, 4.7, 4.5, 4.4, 31.9]

# Crear un lienzo y ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Establecer colores degradados (usar un color diferente para "Otros", y degradados para el resto de las provincias)
color_otros = '#FF6B6B'  # Rojo para "Otros"
colores_provincias = plt.cm.Greens(np.linspace(0.4, 0.9, len(provincias) - 1))
colores = list(colores_provincias) + [color_otros]  # Degradados de provincias primero, seguidos del color para "Otros"

# Dibujar un gráfico de barras horizontales
ancho_barra = 0.6
posicion_y = np.arange(len(provincias))
barras = ax.barh(posicion_y, porcentajes, height=ancho_barra, color=colores, edgecolor='black', alpha=0.8)

# Personalizar el estilo "kebab"
for i, (provincia, porcentaje) in enumerate(zip(provincias, porcentajes)):
    # Calcular el número de cuentas
    cantidad_cuentas = max(1, int(porcentaje * 0.7))  # Determinar el número de cuentas en función del porcentaje

    # Dibujar las cuentas (círculos)
    for j in range(cantidad_cuentas):
        x_cuenta = 0.5 + j * 0.8  # Posición x de la cuenta
        if x_cuenta < porcentaje - 0.5:  # Asegurarse de que las cuentas no excedan el rango de la barra
            # Usar cuentas rojas para el elemento "Otros", y degradados amarillos para el resto
            if i == len(provincias) - 1:
                color_cuenta = plt.cm.Reds(j/cantidad_cuentas)
            else:
                color_cuenta = plt.cm.YlOrRd(j/cantidad_cuentas)
            circulo = mpatches.Circle(
                (x_cuenta, posicion_y[i]),
                radius=0.15,
                color=color_cuenta,
                alpha=0.9
            )
            ax.add_patch(circulo)

    # Agregar etiquetas de provincia (a la izquierda)
    ax.text(-1.5, posicion_y[i], provincia, ha='center', va='center', fontweight='bold', fontsize=11)

# Agregar etiquetas de valores de porcentaje (con cajas de fondo)
for i, rect in enumerate(barras):
    ancho = rect.get_width()
    ax.text(
        ancho + 0.3, rect.get_y() + rect.get_height()/2,
        f'{porcentajes[i]:.1f}%',  # Mantener un decimal
        ha='left', va='center',
        fontweight='bold',
        bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.2')
    )

# Establecer los ejes y el título
ax.set_xlim(-2, max(porcentajes) + 5)  # Ajustar el rango del eje x
ax.set_ylim(-0.8, len(provincias) - 0.2)  # Ajustar el rango del eje y
ax.set_title('La Copa Europea Impulsa la Economía de los Alimentos - Las 10 Provincias Principales en el Monto Total de Consumo de Meriendas Nocturnas', fontsize=16, pad=15, fontweight='bold')
ax.set_xlabel('Proporción de Consumo (%)', fontsize=12, labelpad=10)
ax.set_yticks([])  # Ocultar las etiquetas predeterminadas del eje y

# Agregar líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Agregar una leyenda y moverla hacia abajo
parche_provincia = mpatches.Patch(color=colores_provincias[0], label='Provincias')
parche_otros = mpatches.Patch(color=color_otros, label='Total de Otras Regiones')
ax.legend(handles=[parche_provincia, parche_otros],
          loc='upper right',
          bbox_to_anchor=(0.98, 0.85))  # Ajustar el parámetro bbox_to_anchor para moverla hacia abajo

# Difuminar el borde
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

# Mostrar el gráfico
plt.tight_layout()
plt.show()