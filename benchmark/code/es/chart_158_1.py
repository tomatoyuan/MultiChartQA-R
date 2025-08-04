import matplotlib.pyplot as plt

# Configurar los problemas y porcentajes (en el orden del gráfico original, de mayor a menor)
etiquetas = [
    'Pérdida de agua y sequedad de la piel',
    'Piel opaca',
    'Piel áspera y amarillenta',
    'Pores dilatados',
    'Arrugas y líneas finas',
    'Piel flácida y caída',
    'Depósito de melanina y manchas',
    'Barrera cutánea frágil',
    'Baja capacidad de metabolismo',
    'Otros problemas de envejecimiento',
    'Ninguno de los anteriores'
]
porcentajes = [65, 61, 59, 57, 53, 53, 51, 47, 30, 18, 2]

# Definición de colores (los primeros 3 resaltados en dorado, el resto en púrpura uniforme)
colores = ['#FFCC00', '#FBC02D', '#F9A825'] + ['#673AB7'] * (len(etiquetas) - 3)

# Invertir el orden: mostrar de mayor a menor de arriba hacia abajo
etiquetas = etiquetas[::-1]
porcentajes = porcentajes[::-1]
colores = colores[::-1]
pos_y = range(len(etiquetas))

# Crear la gráfica
fig, ax = plt.subplots(figsize=(10, 7))
barras = ax.barh(pos_y, porcentajes, color=colores)

# Agregar etiquetas de porcentaje
for barra, pct in zip(barras, porcentajes):
    ax.text(barra.get_width() + 1, barra.get_y() + barra.get_height() / 2,
            f'{pct}%', va='center', fontsize=11)

# Configuración del estilo de la gráfica
ax.set_yticks(pos_y)
ax.set_yticklabels(etiquetas, fontsize=11, rotation=20)
ax.invert_yaxis()  # El valor máximo arriba
ax.set_xlim(0, 70)
ax.set_title("La pérdida de agua, el opacamiento y la aspereza amarillenta\n son los problemas de envejecimiento cutáneo más comunes", fontsize=14, weight='bold')

# Eliminar bordes y ejes innecesarios
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.xaxis.set_visible(False)

# Aclaración de la fuente de datos
texto_fuente = (
    "Fuente de datos: Encuesta de CBNData en julio de 2024\n"
    "P4. ¿Encuentra problemas de piel en su vida diaria?"
)
plt.figtext(0.5, -0.05, texto_fuente, wrap=True, ha='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()