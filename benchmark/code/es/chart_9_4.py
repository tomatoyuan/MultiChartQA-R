import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import random

# Establece la semilla aleatoria para garantizar la reproducibilidad de los resultados
np.random.seed(42)
random.seed(42)

# Extrae con precisión los datos del gráfico, los ajusta a números de punto flotante y agrega un ligero desplazamiento aleatorio
# Formato de datos: Provincia: (Ratio de búsqueda, TGI de atención, Región, Color)
province_data = {
    "Jiangxi": (4.2, 171.5, "Central", "#00cc99"),
    "Tianjin": (2.1, 132.3, "Eastern", "#66b3ff"),
    "Guizhou": (1.9, 121.7, "Western", "#ffcc66"),
    "Hebei": (6.3, 120.8, "Eastern", "#66b3ff"),
    "Shandong": (8.9, 131.2, "Eastern", "#66b3ff"),
    "Jiangsu": (10.1, 140.5, "Eastern", "#66b3ff"),
    "Ningxia": (1.0, 110.3, "Western", "#ffcc66"),
    "Shanghai": (3.2, 99.8, "Eastern", "#66b3ff"),
    "Zhejiang": (7.1, 100.4, "Eastern", "#66b3ff"),
    "Guangdong": (9.3, 100.7, "Eastern", "#66b3ff"),
    "Heilongjiang": (1.1, 90.2, "Northeastern", "#ff6666"),
    "Anhui": (2.9, 90.5, "Central", "#00cc99"),
    "Hubei": (4.1, 89.7, "Central", "#00cc99"),
    "Beijing": (3.8, 90.3, "Eastern", "#66b3ff"),
    "Guangxi": (1.2, 80.4, "Western", "#ffcc66"),
    "Hunan": (3.1, 79.8, "Central", "#00cc99"),
    "Jilin": (0.9, 70.6, "Northeastern", "#ff6666"),
    "Fujian": (3.3, 70.1, "Eastern", "#66b3ff"),
    "Chongqing": (1.1, 70.3, "Western", "#ffcc66"),
    "Yunnan": (1.8, 69.7, "Western", "#ffcc66"),
    "Shanxi": (2.2, 60.5, "Central", "#00cc99"),
    "Gansu": (0.8, 50.2, "Western", "#ffcc66"),
    "Xinjiang": (1.0, 40.3, "Western", "#ffcc66"),
    "Qinghai": (1.1, 30.1, "Western", "#ffcc66"),
    "Tibet": (0.9, 20.4, "Western", "#ffcc66"),
    "Henan": (5.2, 100.2, "Central", "#00cc99"),
    "Hainan": (1.0, 99.8, "Eastern", "#66b3ff"),
    "Liaoning": (3.1, 100.3, "Eastern", "#66b3ff"),
    "Sichuan": (5.0, 99.7, "Western", "#ffcc66"),
    "Inner Mongolia": (2.1, 120.5, "Western", "#ffcc66"),
    "Shaanxi": (1.9, 110.2, "Western", "#ffcc66"),
}

# Agrupa por región
region_dict = defaultdict(list)
for prov, (ratio, tgi, region, color) in province_data.items():
    region_dict[region].append((prov, ratio, tgi, color))

# Crea un lienzo
plt.figure(figsize=(10, 7), facecolor='white')
ax = plt.gca()

# Dibuja un gráfico de dispersión (bucle por región)
for region, prov_list in region_dict.items():
    ratios = [d[1] for d in prov_list]
    tgis = [d[2] for d in prov_list]
    colors = [d[3] for d in prov_list]
    ax.scatter(ratios, tgis, c=colors, label=region, s=50, zorder=2)

    # Agrega etiquetas de texto de las provincias (ajusta finamente la posición para evitar superposiciones)
    for d in prov_list:
        prov, ratio, tgi, _ = d
        # Ajusta manualmente las posiciones de las etiquetas de algunas provincias (ajusta según la visión de la imagen original)
        if prov == 'Jiangxi':
            ax.text(ratio + 0.1, tgi - 5, prov, fontsize=9)
        elif prov in ['Tianjin', 'Jiangsu']:
            ax.text(ratio - 0.3, tgi + 2, prov, fontsize=9)
        else:
            ax.text(ratio + 0.1, tgi + 1, prov, fontsize=9)

# Dibuja una línea de referencia para TGI de atención = 100
ax.axhline(y=100, color='gray', linestyle='--', linewidth=1, zorder=1)

# Establece las etiquetas de los ejes
ax.set_xlabel('Ratio de búsqueda(%)', fontsize=12, labelpad=15)
ax.set_ylabel('Atención(TGI)', fontsize=12, labelpad=15)

# Establece el título
ax.set_title('Ratio de búsqueda y atención (TGI) de los usuarios de cada provincia y ciudad por nuevos productos nacionales', fontsize=14, pad=20)

# Ajusta el rango y las marcas de los ejes
ax.set_xlim(0, 11)
ax.set_ylim(0, 180)
ax.set_xticks([1, 3, 5, 7, 9])  # Coincide estrictamente con las marcas del eje x de la imagen original
ax.set_yticks(range(20, 180, 20))

# Establece la leyenda (alinea la posición con la imagen original)
ax.legend(loc='upper right', bbox_to_anchor=(1, 1), frameon=True, fontsize=10)

# Agrega una cuadrícula
ax.grid(linestyle='--', alpha=0.5, zorder=0)

# Optimiza el diseño
plt.tight_layout()
plt.show()