import matplotlib.pyplot as plt

# Datos de provincias
provincias = ["Liaoning", "Jiangsu", "Hubei", "Beijing", "Shandong", "Guangdong", "Zhejiang", "Shanghai", "Sichuan", "Hunan"]
# Número correspondiente de medallas de oro
medallas_de_oro = [36, 29, 26, 22, 22, 22, 16, 15, 14, 14]
# Establece el color del gráfico de barras
color_barra = "#FFD700"  # Color oro, se puede ajustar según sea necesario
# Crea un gráfico de barras
barras = plt.bar(provincias, medallas_de_oro, color=color_barra)
# Añade un título y etiquetas de los ejes, establece el tamaño de fuente
plt.title("Las 10 provincias líderes en medallas de oro olímpicas totales desde los Juegos Olímpicos del 23º al 30º", fontsize=14, fontweight='bold')
plt.xlabel("Provincia", fontsize=12)
plt.ylabel("Número de medallas de oro", fontsize=12)
# Añade anotaciones numéricas
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width() / 2., altura,
             '%d' % int(altura),
             ha='center', va='bottom', fontsize=10)
# Rota las etiquetas de las marcas del eje x para evitar superposiciones, ajusta el ángulo de rotación según la situación real
plt.xticks(rotation=45)
# Muestra el gráfico
plt.tight_layout()  # Optimiza automáticamente el diseño
plt.show()