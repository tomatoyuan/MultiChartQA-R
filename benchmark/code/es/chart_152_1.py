import matplotlib.pyplot as plt
import numpy as np

# Construir la serie temporal
fechas = np.arange('2023-09-01', '2023-12-28', dtype='datetime64[D]')
np.random.seed(0)
base = np.linspace(10, 80, len(fechas)) + np.random.normal(0, 5, len(fechas))

# Crear artificialmente algunos picos para simular "movimientos intensivos en el mercado"
picos = {
    '2023-09-25': 100,
    '2023-10-16': 85,
    '2023-11-07': 90,
    '2023-12-13': 105
}
for fecha, valor in picos.items():
    idx = np.where(fechas == np.datetime64(fecha))[0][0]
    base[idx] = valor

# Crear la gráfica
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(fechas, base, label='Promedio', color='dodgerblue')

# Agregar puntos de resaltado para los picos
fechas_resaltadas = list(picos.keys())
valores_resaltados = [picos[d] for d in fechas_resaltadas]
ax.scatter(fechas_resaltadas, valores_resaltados, color='orange', zorder=5, label='Picos')

# Agregar anotaciones (flecha + descripción + valor)
for i, (fecha, valor) in enumerate(zip(fechas_resaltadas, valores_resaltados)):
    ax.annotate("Período de movimientos intensivos en el mercado SIINSIIN\nÍndice: " + str(valor),
                xy=(np.datetime64(fecha), valor),
                xytext=(0, 50 + i * 10),
                textcoords='offset points',
                arrowprops=dict(arrowstyle="->", color='deeppink'),
                fontsize=9, color='deeppink')

# Configuración de estilo
ax.set_title("Marca SIINSIIN impulsa el mercado de leggins", fontsize=14, pad=50)
ax.set_ylabel("Índice de búsqueda")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.subplots_adjust(top=1.0)  # 给标题腾出空间

plt.show()