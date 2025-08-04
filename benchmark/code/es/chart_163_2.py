# 图二：2024年各业态门店生命周期（月）
etiquetas = ['T1', 'T2', 'T3+']
x = np.arange(len(etiquetas))
ancho = 0.2

# 数据分别为：餐饮、零售、休闲娱乐
restauracion_no_encadenada = [20.7, 22.3, 25.3]
restauracion_encadenada = [24.1, 25.0, 25.4]
retail_no_encadenado = [38.2, 41.2, 43.9]
retail_encadenado = [38.0, 40.5, 43.3]
ocio_no_encadenado = [29.4, 33.7, 34.2]
ocio_encadenado = [32.7, 34.5, 35.9]

fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.bar(x - 0.3, restauracion_no_encadenada, ancho, label='Restauración - \nNo encadenada', color='#B3DE69')
ax2.bar(x - 0.1, restauracion_encadenada, ancho, label='Restauración - \nEncadenada', color='#FCCDE5')
ax2.bar(x + 0.1, retail_no_encadenado, ancho, label='Retail - \nNo encadenado', color='#8DD3C7')
ax2.bar(x + 0.3, retail_encadenado, ancho, label='Retail - \nEncadenado', color='#D9D9D9')

for i in range(len(x)):
    ax2.text(x[i] - 0.3, restauracion_no_encadenada[i] + 0.5, str(restauracion_no_encadenada[i]), ha='center', fontsize=9)
    ax2.text(x[i] - 0.1, restauracion_encadenada[i] + 0.5, str(restauracion_encadenada[i]), ha='center', fontsize=9)
    ax2.text(x[i] + 0.1, retail_no_encadenado[i] + 0.5, str(retail_no_encadenado[i]), ha='center', fontsize=9)
    ax2.text(x[i] + 0.3, retail_encadenado[i] + 0.5, str(retail_encadenado[i]), ha='center', fontsize=9)

ax2.set_xticks(x)
ax2.set_xticklabels(etiquetas)
ax2.set_title('Ciclo de vida de las tiendas de diferentes formatos en 2024 (meses) - Restauración y Retail', fontsize=14)
ax2.set_ylabel('Ciclo de vida (meses)')
ax2.legend()

plt.tight_layout()
plt.show()