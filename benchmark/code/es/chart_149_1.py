import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos (Canales para entender las bebidas sin azúcar)
canales_entendimiento = [
    "Plataformas de comercio electrónico (Taobao, Pinduoduo, etc.)", "Plataformas de videos cortos (Douyin, Kuaishou, etc.)",
    "Plataformas sociales (WeChat, Weibo, etc.)", "Plataformas de videos medianos y largos (Bilibili, iQiyi, etc.)",
    "Carteles o anuncios promocionales fuera de línea", "Recomendaciones de familiares y amigos",
    "Plataformas de compras grupales en la comunidad", "Promociones en tienda"
]
proporciones_entendimiento = [52.1, 49.5, 44.5, 35.6, 33.9, 32.8, 27.2, 24.0]  # Proporción (%)

# Preparación de datos (Proporción de canales de compra en línea de bebidas sin azúcar)
canales_compra = [
    "Plataformas de comercio electrónico \nintegrales (Taobao, JD.com, etc.)", "Nuevas plataformas de comercio \nelectrónico (Douyin, Kuaishou)",
    "Plataformas de supermercados \nen línea (Meituan, Ele.me, etc.)", "Plataformas de compras \ngrupales en la comunidad", "Otros"
]
proporciones_compra = [75.3, 55.8, 67.3, 42.6, 0.4]  # Proporción (%)

# Crear un lienzo (una fila, dos columnas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Dibujar el gráfico de barras de "Canales de entendimiento" a la izquierda ---------------------
x_entendimiento = np.arange(len(canales_entendimiento))
ax1.bar(x_entendimiento, proporciones_entendimiento, color='coral')
ax1.set_title('Canales de entendimiento de bebidas sin azúcar de los consumidores chinos en 2023', fontsize=14)
ax1.set_ylabel('Proporción (%)')
ax1.set_xlabel('Canales de entendimiento')
ax1.set_xticks(x_entendimiento)
ax1.set_xticklabels(canales_entendimiento, rotation=45, ha='right')
ax1.set_ylim(0, 60)  # Ajustar el rango del eje y para adaptarse a la proporción máxima (52.1%)

# Agregar etiquetas numéricas a la izquierda
for i, prop in enumerate(proporciones_entendimiento):
    ax1.text(x_entendimiento[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

# --------------------- Dibujar el gráfico de radar de "Canales de compra en línea" a la derecha ---------------------
# Número de ángulos para el gráfico de radar (correspondiente al número de canales)
num_canales = len(canales_compra)
angulos = np.linspace(0, 2 * np.pi, num_canales, endpoint=False).tolist()
# Cerrar el gráfico de radar (conectar el último punto con el primer punto)
proporciones_compra += proporciones_compra[:1]
angulos += angulos[:1]

ax2 = plt.subplot(1, 2, 2, polar=True)
ax2.fill(angulos, proporciones_compra, color='orange', alpha=0.3)
ax2.plot(angulos, proporciones_compra, color='orange', label='Proporción')

# Establecer las etiquetas del eje (nombres de los canales) del gráfico de radar
ax2.set_xticks(angulos[:-1])
ax2.set_xticklabels(canales_compra)
# Ajustar la escala del eje y (adaptarse al rango de la proporción)
ax2.set_yticks(np.arange(0, 80, 10))
ax2.set_yticklabels(np.arange(0, 80, 10))

# Agregar etiquetas numéricas a la derecha
for i, (angulo, prop) in enumerate(zip(angulos[:-1], proporciones_compra[:-1])):
    ax2.text(angulo, prop + 2, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

ax2.set_title('Proporción de compras en línea de bebidas sin azúcar de los consumidores chinos a través de diferentes canales en 2023', fontsize=14, y=1.1)
ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()