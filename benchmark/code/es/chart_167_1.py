import matplotlib.pyplot as plt

# Configurar los datos
meses = ['Ene\'23', 'Mit\'23', 'Ene\'24']
costo_vida = [57, 63, 63]
economia = [48, 42, 53]
empleo = [38, 57, 48]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(meses, costo_vida, marker='o', label='Aumento del costo de vida', color='#2F66FF')
plt.plot(meses, economia, marker='o', label='Desaceleración económica', color='#0D1C55')
plt.plot(meses, empleo, marker='o', label='Inestabilidad laboral', color='#F97316')

# Agregar etiquetas de datos
for i, valor in enumerate(costo_vida):
    plt.text(meses[i], valor + 1, f'{valor}%', ha='center', va='bottom', fontsize=10, color='#2F66FF')
for i, valor in enumerate(economia):
    plt.text(meses[i], valor + 1, f'{valor}%', ha='center', va='bottom', fontsize=10, color='#0D1C55')
for i, valor in enumerate(empleo):
    plt.text(meses[i], valor + 1, f'{valor}%', ha='center', va='bottom', fontsize=10, color='#F97316')

# Establecer el título y la leyenda
plt.title("Razones por las cuales la situación económica de los consumidores empeora", fontsize=14, pad=20)
plt.legend(loc='upper center', ncol=3, frameon=False, fontsize=10)

# Establecer etiquetas y rangos de los ejes
plt.ylim(30, 70)
plt.ylabel('Proporción (%)')

# Agregar la explicación de los datos y la fuente
plt.figtext(0.5, -0.05, "P: ¿Cuáles son las razones por las cuales su situación financiera ha empeorado?\nFuente: Perspectiva de los consumidores chinos de NIQ 2024", ha='center', fontsize=10)

# Mejorar el diseño
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

plt.show()