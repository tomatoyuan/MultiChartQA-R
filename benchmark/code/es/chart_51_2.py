import matplotlib.pyplot as plt
import numpy as np

# Nombres de las industrias
industrias = ["Tecnología de Alta", "Retail", "Banca", "Transportes Aéreos", "Manufactura de Alta Gama",
              "Bienes de Consumo Empaquetados", "Salud y Bienestar", "Administración", "Energía", "Materiales Básicos",
              "Educación", "Inmuebles", "Semiconductores", "Químicos", "Ingeniería de Infraestructura",
              "Sector Público", "Medios de Comunicación y Entretenimiento", "Productos Farmacéuticos y Médicos",
              "Telecomunicaciones", "Seguros", "Agricultura"]
# Datos de productividad (en miles de millones de dólares), aproximadamente simulados y se pueden ajustar según la situación real
productividad = [450, 390, 340, 300, 290, 270, 260, 250, 240, 230, 200, 180, 170, 140, 150, 110, 110, 110, 100, 70, 70]
# Marcar los índices de las industrias que necesitan un marco especial
indices_especiales = [6, 19]  # Índices correspondientes a Salud y Bienestar, Seguros

x = np.arange(len(industrias))  # Posiciones de las marcas en el eje x
ancho_barra = 0.6  # Ancho de las barras

fig, ax = plt.subplots(figsize=(12, 6))

# Dibujar un gráfico de barras, establecer el color a un verde similar
barras = ax.bar(x, productividad, width=ancho_barra, color='greenyellow')

# Agregar un título
ax.set_title('Mejora de la Productividad de la IA Generativa por Industria')

# Establecer las etiquetas de las marcas en el eje x, girarlas en un cierto ángulo para evitar superposiciones
ax.set_xticks(x)
ax.set_xticklabels(industrias, rotation=45, ha='right')

# Agregar cuadros discontinuos rojos para las industrias especiales
for idx in indices_especiales:
    rect = barras[idx].get_bbox()
    ax.plot([rect.x0, rect.x1, rect.x1, rect.x0, rect.x0],
            [rect.y0, rect.y0, rect.y1, rect.y1, rect.y0],
            'r--', linewidth=1.5)

# Agregar etiquetas numéricas a cada barra
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer la etiqueta del eje y
ax.set_ylabel('Productividad (Miles de Millones de Dólares)')

plt.tight_layout()  # Ajustar automáticamente el diseño para evitar superposiciones de etiquetas
plt.show()