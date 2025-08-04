import matplotlib.pyplot as plt
import numpy as np

# Establecer datos trimestrales
trimestres = ['T1 2023', 'T2 2023', 'T3 2023', 'T4 2023', 'T1 2024', 'T2 2024']
# Datos de volumen de descargas de la App Store (en cientos de millones), ajustados para que T1 2024 + T2 2024 ≈ 1.76
app_store = [0.77, 0.8, 0.95, 0.85, 0.95, 0.81]
# Datos de volumen de descargas de Google Play (en cientos de millones), ajustados para que T1 2024 + T2 2024 ≈ 1.44
google_play = [0.8, 0.75, 0.75, 0.8, 0.8, 0.64]

x = np.arange(len(trimestres))  # Posiciones de las marcas en el eje x
ancho = 0.5  # Aumentar el ancho de las barras

# Crear un gráfico más ancho (ancho 12, alto 6)
fig, ax = plt.subplots(figsize=(12, 6))

# Dibujar las barras de la App Store (en la parte inferior)
rects1 = ax.bar(x, app_store, ancho, label='App Store', color='#9b59b6')
# Dibujar las barras de Google Play (en la parte superior)
rects2 = ax.bar(x, google_play, ancho, bottom=app_store, label='Google Play', color='#1abc9c')

# Establecer las etiquetas de las marcas en el eje x y el ángulo de rotación
ax.set_xticks(x)
ax.set_xticklabels(trimestres, rotation=0)  # Mostrar las etiquetas trimestrales horizontalmente

# Establecer el rango y las marcas en el eje y
ax.set_ylim(0, 2.0)
ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_yticklabels(['000M', '50M', '100M', '150M', '200M'])

# Agregar etiquetas de datos (modificado para mantener dos decimales)
def agregar_etiquetas(rects, valores_inferiores=None):
    for i, rect in enumerate(rects):
        altura = rect.get_height()
        if valores_inferiores is not None:
            pos_y = valores_inferiores[i] + altura / 2
        else:
            pos_y = altura / 2
        # Formatear para mostrar dos decimales
        ax.text(rect.get_x() + rect.get_width()/2., pos_y,
                f'{altura:.2f}', ha='center', va='center', color='white', fontweight='bold')

agregar_etiquetas(rects1)  # Etiquetas de la App Store
agregar_etiquetas(rects2, app_store)  # Etiquetas de Google Play

# Agregar leyenda y título
ax.legend(loc='upper right')
ax.set_title('Tendencia de descargas de juegos móviles en el mercado japonés desde T1 2023 hasta T2 2024', fontsize=16, pad=20)

# Agregar líneas de cuadrícula
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar el texto especificado debajo del título (ajustar la coordenada y a 0.92)
texto = "En el primer semestre de 2024, el número de descargas de juegos móviles en el mercado japonés aumentó un 2.5% año tras año, \nalcanzando 320 millones, de los cuales la plataforma App Store representó el 55% de las descargas."
fig.text(0.5, 0.90, texto, ha='center', va='center', fontsize=12)

# Ajustar el diseño
plt.tight_layout()

plt.show()