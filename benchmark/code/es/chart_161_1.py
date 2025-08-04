import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Datos
categorias = {
    'Cuidado de la piel': {
        'etiquetas': ['Cuidado facial', 'Sets de cuidado \nde la piel', 'Mascarillas', 'Limpieza facial', 'Tónicos', 'Cuidado de\n los ojos', 'Protección solar', 'Otros de cuidado\n de la piel', 'Cuidado de \nlos labios'],
        'valores': [38, 23, 12, 9, 5, 5, 5, 1, 1],
        'color': 'Reds'
    },
    'Maquillaje': {
        'etiquetas': ['Maquillaje facial', 'Maquillaje labial', 'Maquillaje ocular', 'Herramientas de\n maquillaje', 'Sets de maquillaje', 'Uñas'],
        'valores': [47, 24, 12, 10, 6, 1],
        'color': 'Blues'
    },
    'Perfumes': {
        'etiquetas': ['Perfumes'],
        'valores': [100],
        'color': 'Greens'
    }
}

# Inicializar la gráfica
fig, ax = plt.subplots(figsize=(16,10))
y_base = 0
altura_barra = 0.6
espacio_grupo = 1.2
relleno_etiqueta = 0.5

# Bucle principal de trazado
for indice_grupo, (grupo, contenido) in enumerate(categorias.items()):
    etiquetas = contenido['etiquetas']
    valores = contenido['valores']
    mapa_color = plt.get_cmap(contenido['color'])
    num_elementos = len(valores)

    # Escala de colores
    colores = [mapa_color(0.3 + 0.6 * i / max(len(valores)-1, 1)) for i in range(len(valores))]

    # Bloque de fondo
    ax.add_patch(
        patches.Rectangle(
            (-10, y_base - altura_barra/2 - 0.3),
            110, num_elementos * (altura_barra + 0.2),
            color=mapa_color(0.05), zorder=0
        )
    )

    # Etiqueta del nombre del grupo a la izquierda
    ax.text(-15, y_base + (num_elementos - 1) * (altura_barra + 0.2)/2,
            f'{grupo}', va='center', ha='center',
            fontsize=13, weight='bold', bbox=dict(facecolor=mapa_color(0.2), boxstyle='round,pad=0.4', edgecolor='none'))

    for i, (etiqueta, valor) in enumerate(zip(etiquetas, valores)):
        y = y_base + i * (altura_barra + 0.2)
        ax.barh(y, valor, height=altura_barra, color=colores[i], edgecolor='black')
        ax.text(valor + 1, y, f'{valor}%', va='center', ha='left', fontsize=10)
        ax.text(-0.5, y, etiqueta, va='center', ha='right', fontsize=10)

    y_base += num_elementos * (altura_barra + 0.2) + espacio_grupo

# Configuración de formato
ax.set_xlim(-10, 110)
ax.set_ylim(-1, y_base)
ax.set_xticks(range(0, 101, 20))
ax.set_xticklabels([f'{x}%' for x in range(0, 101, 20)])
ax.set_yticks([])
ax.set_xlabel('Porcentaje (%)', labelpad=15)
ax.set_title('Distribución del tamaño de las subcategorías del mercado\n'
             ' minorista electrónico en el primer trimestre de 2024 (nivel 2)', fontsize=14, weight='bold')
ax.invert_yaxis()
plt.tight_layout()
plt.show()