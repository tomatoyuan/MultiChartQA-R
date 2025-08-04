import matplotlib.pyplot as plt
import numpy as np

# Meses
meses = ["2021.4", "2021.5", "2021.6", "2021.7", "2021.8", "2021.9", "2021.10", "2021.11", "2021.12"]
# Índice de facturación mensual de productos de belleza y cuidado del cabello en Tmall y Taobao (datos simulados)
tmall_taobao = [1400000000, 1200000000, 2200000000, 1100000000, 1500000000, 1700000000, 1300000000, 3200000000, 1400000000]
# Índice de facturación mensual de productos de belleza y cuidado del cabello en Tmall Global (datos simulados)
tmall_global = [500000000, 500000000, 900000000, 400000000, 600000000, 600000000, 500000000, 1400000000, 500000000]
# Datos de crecimiento anual
crecimiento_anual = "+12.3%"
descripcion_crecimiento_anual = "Crecimiento anual de la facturación (índice) del mercado de belleza y cuidado del cabello"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 5000000000)

# Dibujar un gráfico de líneas para Tmall y Taobao
ax.plot(meses, tmall_taobao, marker='o', color="#A4C639", label="Índice de facturación mensual de productos de belleza y cuidado del cabello en Tmall y Taobao", linewidth=2)
# Dibujar un gráfico de líneas para Tmall Global
ax.plot(meses, tmall_global, marker='o', color="#87CEEB", label="Índice de facturación mensual de productos de belleza y cuidado del cabello en Tmall Global", linewidth=2)

# Agregar etiquetas de datos (simplificado, se puede mejorar según sea necesario)
for x, y in zip(meses, tmall_taobao):
    ax.annotate(f'{y/1000000000:.1f} mil millones',
                xy=(x, y),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")
for x, y in zip(meses, tmall_global):
    ax.annotate(f'{y/1000000000:.1f} mil millones',
                xy=(x, y),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#87CEEB")

# Establecer la etiqueta del eje y
ax.set_ylabel("Índice de facturación")
# Establecer el título
ax.set_title("Tendencia del índice de facturación mensual de productos de belleza y cuidado del cabello en China en 2021", fontsize=14, fontweight='bold')

# Agregar una leyenda
ax.legend(loc='upper right')

# Embelezar: Ocultar los bordes superior y derecho
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()