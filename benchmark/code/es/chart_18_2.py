import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
etiquetas = ["Banquete", "Cavalcada", "Maestro de ceremonias", "Suministros de boda", "Otros", "Luna de miel", "Joyas", "Fotos de boda"]
tamaños = [6, 0.8, 0.2, 1.5, 5, 4, 3, 1]
costo_total = sum(tamaños)  # Costo total

# Esquema de colores optimizado (utilizando colores de gradiente más armoniosos)
colores = plt.cm.YlOrRd(np.linspace(0.2, 0.9, len(etiquetas)))

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 8))

# Dibujar un gráfico de dona
porciones, textos, textos_automaticos = ax.pie(
    tamaños, 
    labels=None,  # No mostrar etiquetas directamente en el gráfico
    colors=colores,
    autopct='',  # No mostrar valores por ahora
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2)  # Aumentar el ancho del anillo y agregar un borde blanco
)

# Personalizar etiquetas: mostrar tanto el nombre como la cantidad, y ajustar inteligentemente la posición y el color
for i, (porcion, etiqueta, tamaño) in enumerate(zip(porciones, etiquetas, tamaños)):
    # Calcular la posición del texto
    theta = (porcion.theta2 + porcion.theta1) / 2
    x = 0.65 * np.cos(np.radians(theta))  # 0.65 controla la posición radial
    y = 0.65 * np.sin(np.radians(theta))
    
    # Ajustar el estilo del texto según el tamaño del sector
    tamaño_texto = 10 if tamaño / costo_total > 0.05 else 8  # Usar una fuente más pequeña para sectores pequeños
    
    # Contenido del texto
    texto = f"{etiqueta}\n{ tamaño} millones de yuanes"
    
    # Ajustar el color del texto (usar texto blanco para sectores oscuros y texto negro para sectores claros)
    color = 'white' if i in [0, 4, 5, 6] else 'black'
    
    # Agregar texto
    ax.text(x, y, texto, ha='center', va='center', fontsize=tamaño_texto, 
            fontweight='bold', color=color, bbox=dict(
                boxstyle="round,pad=0.2", 
                fc=colores[i], 
                ec='none', 
                alpha=0.7
            ))

# Establecer el título
ax.set_title("Distribución de gastos de boda de la Sra. Liu en Shanghái", fontsize=18, fontweight='bold', pad=20)
subtitulo = f"Costo total: {costo_total} millones de yuanes"
plt.figtext(0.5, 0.92, subtitulo, ha='center', fontsize=12, color='gray')

# Agregar texto en el centro
circulo_centro = plt.Circle((0, 0), 0.2, fc='white')
ax.add_patch(circulo_centro)
ax.text(0, 0, "Gastos de boda", ha='center', va='center', fontsize=14, fontweight='bold')

# Ajustar el diseño
plt.tight_layout()

# Agregar la fuente de datos
plt.figtext(0.5, 0.01, "Fuente de datos: Ejemplo hipotético", ha='center', fontsize=8, color='gray')

plt.show()