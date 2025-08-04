import matplotlib.pyplot as plt

# Datos
etiquetas = ['Sector Industrial', 'Transporte', 'Construcción y Otros Sectores']
tamaños = [60, 31, 9]
colores = ['#A4C639', '#a8dda8', '#87CEEB']  # Coincidir con el tono de color original

# Crear lienzo
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar gráfico circular
wedges, textos, autotextos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.1f%%',  
    startangle=90,     
    colors=colores,
    textprops={'color': 'black'}
)

# Ajustar posiciones de las etiquetas (colocar la etiqueta "Sector Industrial" fuera del gráfico circular para coincidir con el diseño original)
for texto, autotexto, wedge in zip(textos, autotextos, wedges):
    if texto.get_text() == 'Sector Industrial':
        texto.set_position((1.15, 0.5))  
        autotexto.set_position((1.3, 0.5))

# Agregar cuadro de descripción de la estructura encima
texto_estructura = "Sector Industrial: 60%\nTransporte: 31%\nConstrucción y Otros: 9%"
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="green", lw=1)
ax.text(0.25, 0.1, texto_estructura, transform=ax.transAxes, fontsize=12,
        bbox=bbox_props, color='green')

# Establecer título
ax.set_title('Estructura de Utilización de Hidrógeno', fontsize=14, fontweight='bold', y=1.1)

plt.tight_layout()
plt.show()