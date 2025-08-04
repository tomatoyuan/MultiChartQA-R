import matplotlib.pyplot as plt

# 数据
etiquetas = [
    'Oportunidades de expansión y\n'
    ' crecimiento del mercado',
    'Servicio al cliente',
    'Transformación y innovación',
    'Promoción del desarrollo sostenible',
    'Cadena de suministro',
    'Recursos tecnológicos y humanos',
    'Cambios en la demanda del mercado',
    'Impacto de las políticas',
    'Otros'
]
valores = [55, 19, 7, 6, 4, 3, 3, 2, 1]
colores = ['orange', 'orange'] + ['#0070C0'] * 7  # Los dos primeros naranja, los siguientes azules

# Cuerpo del gráfico
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.barh(etiquetas[::-1], valores[::-1], color=colores[::-1])

# Agregar etiquetas de porcentaje
for barra in barras:
    ax.text(barra.get_width() + 1, barra.get_y() + barra.get_height()/2,
            f'{barra.get_width():.0f}%', va='center', fontsize=11)

# Configurar etiquetas de los ejes y título
ax.set_xlim(0, 60)
ax.set_xlabel('Porcentaje (%)', fontsize=12)
ax.set_title('Factores motores principales para la internacionalización de empresas chinas en la etapa actual', fontsize=14, pad=15)

# Eliminar los bordes del gráfico
ax.spines[['top', 'right']].set_visible(False)

# Agregar leyenda y fuente de los datos
plt.figtext(0.01, -0.04, 'Leyenda: Factores motores principales para la internacionalización de empresas chinas en la etapa actual',
            fontsize=10, ha='left')
plt.figtext(0.01, -0.08, 'Fuente de datos: Deloitte, compilado por el Instituto de 36Kr',
            fontsize=10, ha='left')

plt.tight_layout()
plt.show()