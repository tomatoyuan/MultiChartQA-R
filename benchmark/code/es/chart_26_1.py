import matplotlib.pyplot as plt

# Datos
etiquetas = ['Mujer', 'Hombre']
tamaños = [35, 65]
colores = ['#FF69B4', '#4169E1']  # Corresponde a rosa y azul
resaltar = (0.05, 0)  # Resaltar la parte de las mujeres

# Crear un lienzo y sub - gráfico
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#666666')

# Dibujar un gráfico de donut
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    explode=resaltar,
    colors=colores,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(tamaños)/100)})',  # Mostrar porcentaje y cantidad real
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2),
    textprops=dict(fontsize=12)
)

# Establecer el título y subtítulo
ax.set_title('Análisis de la proporción de género en búsquedas de regalos de San Valentín', fontsize=18, fontweight='bold', pad=20)

# Mejorar el estilo del texto - Versión corregida (usando textos y textos_automaticos devueltos por el gráfico de pastel)
for texto in textos:
    texto.set_color('#666666')  # Texto de color gris oscuro
    texto.set_fontsize(14)
    texto.set_fontweight('bold')

for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white')  # Mantener el texto del porcentaje en blanco (para contraste con el fondo oscuro)
    texto_automatico.set_fontsize(12)
    texto_automatico.set_fontweight('bold')

# Agregar una leyenda y una anotación
ax.legend(porciones, etiquetas, title="Género", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.annotate(
    'Mayor proporción de búsquedas por hombres',
    xy=(0.5, 0.5),
    xytext=(0.7, 0.7),
    arrowprops=dict(arrowstyle='->', color='#333333'),
    fontsize=12,
    ha='center'
)

# Establecer el fondo y el diseño
plt.tight_layout()
plt.subplots_adjust(right=0.8)  # Hacer espacio para la leyenda
plt.axis('equal')  # Asegurar que el gráfico de pastel sea circular

# Guardar el gráfico (opcional)
# plt.savefig('valentines_gift_gender_pie.png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()