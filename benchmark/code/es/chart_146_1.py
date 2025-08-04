import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
canales_online = ["Plataformas de comercio electrónico", "Comercio a través de transmisiones en vivo", "Comercio a través de vídeos cortos", "Comercio a través de WeChat", "Otros"]
porcentajes_online = [69.4, 15.2, 10.3, 4.7, 0.4]

canales_offline = ["Centros comerciales y supermercados", "Tiendas de conveniencia", "Calles peatales", "Puestos callejeros", "Otros"]
porcentajes_offline = [65.8, 55.0, 49.8, 26.2, 0.0]

# Configurar el lienzo y los subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar el gráfico de barras para los canales de compra online
x1 = np.arange(len(canales_online))
barras1 = ax1.bar(x1, porcentajes_online, color='orange')
ax1.set_title('Canales de compra online')
ax1.set_ylabel('Proporción (%)')
ax1.set_xticks(x1)
ax1.set_xticklabels(canales_online, rotation=45, ha='right')

# Agregar etiquetas de valor para los canales de compra online
for barra in barras1:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2., altura + 0.5,
             f'{altura}%', ha='center', va='bottom')

# Dibujar el gráfico de barras para los canales de compra offline
x2 = np.arange(len(canales_offline))
barras2 = ax2.bar(x2, porcentajes_offline, color='gold')
ax2.set_title('Canales de compra offline')
ax2.set_ylabel('Proporción (%)')
ax2.set_xticks(x2)
ax2.set_xticklabels(canales_offline, rotation=45, ha='right')

# Agregar etiquetas de valor para los canales de compra offline
for barra in barras2:
    altura = barra.get_height()
    ax2.text(barra.get_x() + barra.get_width()/2., altura + 0.5,
             f'{altura}%', ha='center', va='bottom')

plt.suptitle('Distribución de los canales de compra nocturna online y offline entre los residentes chinos en 2023', fontsize=16, y=1.03)
plt.tight_layout()
plt.show()