import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2024e", "2025e", "2026e", "2027e", "2028e", "2029e"]

# Datos de inversión para cada tecnología (en miles de millones de yuanes), en el orden de RPA/IPA, Otros, IA, Nube, Big Data
# Nota: El último valor se calcula restando los valores anteriores del total para asegurar que la suma de cada capa sea correcta
tech_investment = np.array([
    [12.2, 25.8, 61.1, 117.9 - (12.2 + 25.8 + 61.1)],  # Total en 2024e: 12.2+25.8+61.1+18.8=117.9
    [14.6, 32.3, 73.7, 144.9 - (14.6 + 32.3 + 73.7)],  # Total en 2025e: 14.6+32.3+73.7+24.3=144.9
    [17.5, 40.3, 88.5, 177.2 - (17.5 + 40.3 + 88.5)],  # Total en 2026e: 17.5+40.3+88.5+30.9=177.2
    [20.7, 49.9, 105.5, 215.3 - (20.7 + 49.9 + 105.5)],# Total en 2027e: 20.7+49.9+105.5+39.2=215.3
    [24.8, 62.3, 126.9, 263.8 - (24.8 + 62.3 + 126.9)],# Total en 2028e: 24.8+62.3+126.9+50.0=263.8
    [29.3, 54.0, 153.6, 325.4 - (29.3 + 54.0 + 153.6)] # Total en 2029e: 29.3+54.0+153.6+88.5=325.4
])

# Colores correspondientes a cada tecnología (tan cercanos como sea posible a la imagen original)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Nombres de las tecnologías (con unidades)
tech_names = ["RPA/IPA", "Otros", "IA", "Nube", "Big Data"]

x = np.arange(len(years))  # Posiciones de las marcas en el eje x
bar_width = 0.6  # Ancho del gráfico de barras

fig, ax = plt.subplots(figsize=(12, 7))

# Dibujar el gráfico de barras apiladas
bottom = np.zeros(len(years))
for i in range(tech_investment.shape[1]):
    bars = ax.bar(x, tech_investment[:, i], width=bar_width, bottom=bottom, 
                  color=colors[i], label=tech_names[i])
    bottom += tech_investment[:, i]
    
    # Etiquetar los valores en cada capa apilada
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 0:  # Etiquetar solo valores no nulos
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                bar.get_y() + height/2,
                f'{height:.1f}',
                ha='center', va='center',
                color='white', fontsize=9, fontweight='bold'
            )

# Agregar el título
ax.set_title('Inversión en tecnologías de vanguardia de la industria de seguros en China de 2024 a 2029', fontsize=14, pad=15)

# Establecer las etiquetas de las marcas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)

# Agregar la etiqueta del eje y
ax.set_ylabel('Inversión en tecnologías (Miles de millones de yuanes)', fontsize=12)

# Agregar la leyenda (ubicada en el lado derecho del gráfico)
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=10)

# Calcular y etiquetar la TIR (22.5%)
cagr = 22.5
start_value = tech_investment[0].sum()
end_value = tech_investment[-1].sum()

# Dibujar la línea de la TIR
ax.plot([x[0], x[-1]], [start_value, end_value], 'gray', linestyle='--', linewidth=1.2)

# Agregar la etiqueta de texto de la TIR
ax.annotate(
    f'TIR={cagr}%', 
    xy=(x[2], start_value + (end_value - start_value)*0.4), 
    xytext=(x[2]+0.5, start_value + (end_value - start_value)*0.6),
    arrowprops=dict(facecolor='gray', shrink=0.05, width=1.2, headwidth=8),
    fontsize=11,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
)

# Embelezar el gráfico
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Agregar líneas de cuadrícula horizontales
plt.tight_layout()  # Ajustar automáticamente el diseño

plt.show()