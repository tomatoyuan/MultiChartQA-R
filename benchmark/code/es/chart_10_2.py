import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Proporción de búsquedas de formación profesional en PC', 'Proporción de búsquedas de formación profesional en móvil']
tamaños = [19.30, 80.70]
# Un esquema de colores más moderno
colores = ['#3498db', '#e74c3c']  
# Destacar la parte móvil
explode = (0, 0.05)  

# Crear una figura y ejes, establecer el tamaño de la figura
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de donut, agregar efecto de sombra y optimizar el formato del texto de porcentaje
wedges, textos, autotextos = ax.pie(tamaños, 
                                explode=explode,
                                labels=etiquetas,
                                autopct=lambda p: f'{p:.2f}%\n({p*sum(tamaños)/100:.1f})',
                                startangle=90,
                                colors=colores,
                                wedgeprops={'width': 0.4, 'edgecolor': 'w', 'linewidth': 2},
                                shadow=True,
                                textprops={'fontsize': 12})

# Establecer el título y la leyenda
ax.set_title('Análisis de la proporción de terminales de búsqueda de formación profesional', fontsize=16, pad=20)
ax.legend(wedges, etiquetas, title="Tipo de terminal", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Optimizar el estilo del texto de porcentaje - cambiar el color a oscuro
plt.setp(autotextos, size=12, weight="bold", color='black')  # Cambiar el color a negro
plt.setp(textos, size=12)

# Establecer el fondo de la figura y el diseño
plt.tight_layout()
plt.axis('equal')  # Asegurar que el gráfico de pastel sea circular
plt.subplots_adjust(right=0.8)  # Hacer espacio para la leyenda

# Guardar la figura (opcional)
# plt.savefig('Proporción de terminales de búsqueda de formación profesional.png', dpi=300, bbox_inches='tight')

# Mostrar la figura
plt.show()