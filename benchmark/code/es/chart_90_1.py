import matplotlib.pyplot as plt

# Datos
trimestres = ["2021T2", "2021T3", "2021T4", "2022T1"]
ventas = [7.0, 5.0, 4.2, 10.9]
colores = ['#AED581', '#81C784', '#4DB6AC', '#9575CD']  # Esquema de colores suaves

# Crear un lienzo
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de donut
porciones, textos, textos_automaticos = ax.pie(
    ventas, 
    labels=trimestres, 
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    wedgeprops=dict(width=0.6, edgecolor='white')
)

# Embelezar los textos de porcentaje
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white')
    texto_automatico.set_fontweight('bold')
    texto_automatico.set_fontsize(10)

# Agregar el texto de ventas totales al centro
ventas_totales = sum(ventas)
ax.text(0, 0, f'{ventas_totales:.1f} Mil millones\nVentas Totales',
        ha='center', va='center',
        fontsize=13, fontweight='bold',
        color='#424242')

# Establecer el título
ax.set_title("Proporción de ventas de cerveza en comercio electrónico desde 2021T2 hasta 2022T1 (Unidad: Mil millones de yuanes)", fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.show()