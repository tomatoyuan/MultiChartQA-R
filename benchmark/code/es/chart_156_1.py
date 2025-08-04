import matplotlib.pyplot as plt
import numpy as np

# Años y datos de cuota
years = ['MAT2022', 'MAT2023', 'MAT2024']
top5 = np.array([27, 34, 37])
top6_10 = np.array([15, 13, 11])
top11_20 = np.array([13, 12, 11])
others = 100 - (top5 + top6_10 + top11_20)

# Posición de las barras apiladas
x = np.arange(len(years))
bar_width = 0.6

# Crear la figura
fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(top=0.88)

# Dibujar el gráfico de barras apiladas
p1 = ax.bar(x, top5, bar_width, label='TOP5', color='#FF7F7F')
p2 = ax.bar(x, top6_10, bar_width, bottom=top5, label='TOP6-10', color='#FFBFA2')
p3 = ax.bar(x, top11_20, bar_width, bottom=top5+top6_10, label='TOP11-20', color='#FFD6A5')
p4 = ax.bar(x, others, bar_width, bottom=top5+top6_10+top11_20, label='Otros', color='#D3D3D3')

# Agregar etiquetas de valor a todas las partes
for i in range(len(years)):
    # TOP5
    ax.text(x[i], top5[i] / 2, f"{top5[i]}%", ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # TOP6-10
    ax.text(x[i], top5[i] + top6_10[i] / 2, f"{top6_10[i]}%", ha='center', va='center',
            fontsize=10, color='black')

    # TOP11-20
    ax.text(x[i], top5[i] + top6_10[i] + top11_20[i] / 2, f"{top11_20[i]}%", ha='center', va='center',
            fontsize=10, color='black')

    # Otros
    ax.text(x[i], 100 - others[i] / 2, f"{others[i]}%", ha='center', va='center',
            fontsize=10, color='black')

# Configurar los ejes y el título
ax.set_title('Cambio en la cuota de marca de los "calcetines de efecto pierna desnuda" \nen la plataforma Taobao en línea de MAT2022 a MAT2024', fontsize=15, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.set_ylabel('Cuota de marca (%)', fontsize=12)
ax.set_ylim(0, 100)

# Agregar la nota de fuente de datos
source_text = ("Fuente de datos: Datos de Magic Mirror Market Intelligence, \n"
               "MAT2024: de julio de 2023 a junio de 2024"
               "Explicación de los datos: La lógica de extracción de datos es \n"
               "los datos de consumo de productos que contienen palabras clave\n"
               " como 'calcetines de efecto pierna desnuda' en el título de los\n"
               " productos de la categoría 'Medias de tobillo/compresión' en las\n"
               " plataformas Tmall/Taobao/Douyin;"
               "\n\nBig Data: Total Insight")
plt.figtext(0.5, -0.2, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

# Leyenda y estilo
ax.legend(loc='upper right', frameon=False)
ax.set_facecolor('#f9f9f9')
plt.tight_layout()
plt.show()