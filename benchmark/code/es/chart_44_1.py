import matplotlib.pyplot as plt

# Datos
etiquetas = [
    "Hay muy pocas opciones de almuerzo. He comido \nen los mismos pocos lugares tantas veces que ya me cansé de ellos.",
    "Estoy preocupado por los problemas de salud de la comida para llevar, \npero no hay otras opciones además de la comida para llevar.",
    "Debido al trabajo ocupado, a menudo no tengo tiempo \npara almorzar o no puedo almorzar a tiempo.",
    "Quiero comer comida saludable y deliciosa, \npero no hay canales de compra o los precios son caros."
]
tamaños = [53, 44, 41, 40]
colores = ['#7ccf7c', '#7ccf7c', '#7ccf7c', '#7ccf7c']  # Serie verde

# Crear lienzo
plt.figure(figsize=(12, 8))

# Dibujar gráfico de barras horizontales
barras = plt.barh(etiquetas, tamaños, color=colores, alpha=0.8)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    plt.text(ancho + 1, barra.get_y() + barra.get_height()/2,
             f'{ancho}%',
             ha='left', va='center', fontsize=12)

# Establecer título y etiquetas
plt.title("Poco tiempo, opciones limitadas. Difícil asegurar 'ingesta saludable' incluso con esfuerzo.", fontsize=14, fontweight='bold')
plt.xlabel('Porcentaje (%)', fontsize=12)
plt.ylabel('Tipo de problema', fontsize=12)

# Establecer rango del eje x
plt.xlim(0, 60)

# Agregar líneas de cuadrícula
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Optimizar el diseño
plt.tight_layout()

# Mostrar gráfico
plt.show()