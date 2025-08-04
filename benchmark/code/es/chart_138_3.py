import matplotlib.pyplot as plt

# Datos de Haidilao
haidilao_etiquetas = ["Primera categoría", "Nueva primera categoría", "Segunda categoría", "Tercera categoría", "Cuarta categoría", "Quinta categoría", "Otro"]
haidilao_tamaños = [17.3, 30.1, 21.7, 16.9, 8.5, 4.0, 1.5]
haidilao_provincias = {"Provincia de Guangdong": 162, "Provincia de Zhejiang": 111, "Provincia de Shandong": 77}
haidilao_colores = ["#FF7F50", "#FFD700", "#32CD32", "#8B4513", "#9370DB", "#8B8B83", "#F4A460"]

# Datos de Xiaolongkan
xiaolongkan_etiquetas = ["Primera categoría", "Nueva primera categoría", "Segunda categoría", "Tercera categoría", "Cuarta categoría", "Quinta categoría", "Otro"]
xiaolongkan_tamaños = [8.9, 18.8, 24.0, 8.3, 25.7, 13.0, 1.3]
xiaolongkan_provincias = {"Provincia de Anhui": 76, "Provincia de Guangdong": 62, "Provincia de Jiangsu": 44}
xiaolongkan_colores = ["#FF7F50", "#FFD700", "#32CD32", "#8B4513", "#9370DB", "#8B8B83", "#F4A460"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar el gráfico circular de Haidilao
wedges, texts, autotexts = ax1.pie(haidilao_tamaños, colors=haidilao_colores, autopct='%1.1f%%', startangle=90,
                                    wedgeprops=dict(width=0.4))
ax1.set_title('Distribución de tiendas de Haidilao')
# Dibujar la caja de texto de las provincias
texto_provincia = "\n".join([f"{provincia}: {count} tiendas" for provincia, count in haidilao_provincias.items()])
ax1.text(-1.5, 0.8, texto_provincia, fontsize=10, bbox=dict(facecolor='white', edgecolor='orange', boxstyle='round,pad=0.5'))
# Ajustar la leyenda y colocarla a la derecha del gráfico circular
ax1.legend(wedges, haidilao_etiquetas, title="Categoría de ciudad", loc="center left", bbox_to_anchor=(1, 0.5))
# Hacer que el color del texto de la anotación sea más claro (distinguir entre sectores oscuros/claros)
for autotext in autotexts:
    autotext.set_color('black' if autotext.get_position()[1] > 0.5 else 'black')

# Dibujar el gráfico circular de Xiaolongkan
wedges2, texts2, autotexts2 = ax2.pie(xiaolongkan_tamaños, colors=xiaolongkan_colores, autopct='%1.1f%%', startangle=90,
                                      wedgeprops=dict(width=0.4))
ax2.set_title('Distribución de tiendas de Xiaolongkan')
# Dibujar la caja de texto de las provincias
texto_provincia2 = "\n".join([f"{provincia}: {count} tiendas" for provincia, count in xiaolongkan_provincias.items()])
ax2.text(0.3, 0.8, texto_provincia2, fontsize=10, ha='right',
         bbox=dict(facecolor='white', edgecolor='orange', boxstyle='round,pad=0.5'))
ax2.legend(wedges2, xiaolongkan_etiquetas, title="Categoría de ciudad", loc="center right", bbox_to_anchor=(-0.2, 0.5))
for autotext in autotexts2:
    autotext.set_color('black' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('Distribución de tiendas de algunas marcas populares de fondue en China en 2023', fontsize=14)
plt.tight_layout()
plt.show()