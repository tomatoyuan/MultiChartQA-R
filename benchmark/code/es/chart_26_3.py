import matplotlib.pyplot as plt

# Datos
etiquetas = ["Relación no determinada con persona de sexo opuesto", "Novio", "Esposo"]
valores = [119, 1115, 139]

# Crear un gráfico de barras con tamaño de figura ajustado
plt.figure(figsize=(9, 6))  # Aumentar el ancho para acomodar las etiquetas inclinadas
barras = plt.bar(etiquetas, valores, color="#F48FB1")  # Color basado en rosa

# Configurar el ángulo de inclinación y la alineación de las etiquetas del eje x
plt.xticks(rotation=30, ha='right', fontsize=11)  # Inclinación de 30 grados + alineación a la derecha

# Agregar título y etiquetas
plt.title("Proporción de destinatarios de regalos de mujeres", fontsize=16, fontweight="bold")
plt.xlabel("Destinatarios de regalos", fontsize=12)
plt.ylabel("Cantidad", fontsize=12)

# Mostrar los valores encima de las barras
for i, v in enumerate(valores):
    plt.text(i, v + 20, str(v), ha="center", fontsize=10)  # Ajustar la posición de las etiquetas de valor

# Ocultar los bordes superior y derecho para mejorar el aspecto visual
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Optimizar el diseño y mostrar el gráfico
plt.tight_layout()
plt.show()