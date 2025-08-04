import matplotlib.pyplot as plt
import numpy as np

# Canales de información
canales = ["Weibo/WeChat", "Plataformas de videos cortos como Douyin y Kuaishou", "Plataformas de información como Toutiao y Baidu Hao", "Radio y TV", 
           "Sitios web oficiales de medios financieros", "Periódicos/Revistas", "Aplicaciones de medios financieros", "Blogs financieros/Sitios web personales", 
           "Proveedores profesionales de datos financieros (Wind Information, Flush, etc.)"]
# Proporciones correspondientes (%)
proporciones = [45.61, 44.08, 43.97, 34.32, 31.91, 24.67, 24.23, 18.64, 13.27]

x = np.arange(len(canales))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(canales, rotation=15, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Canales por los que los usuarios de noticias financieras chinos obtienen información de medios financieros en 2025')

plt.tight_layout()
plt.show()