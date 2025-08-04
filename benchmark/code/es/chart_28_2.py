import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Datos: Provincias y cantidades correspondientes de carritos de compra
data = {
    "Guangdong": 6,
    "Zhejiang": 3,
    "Beijing": 2
}
# Coordenadas de las provincias (posición en el eje y, controla la disposición vertical)
province_y = {
    "Guangdong": 2,
    "Zhejiang": 1,
    "Beijing": 0
}
# Tamaño básico del carrito de compra
cart_width = 0.3
cart_height = 0.2

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 7)
ax.set_ylim(-1, 3)
ax.axis('off')  # Ocultar los ejes

# Dibujar el título - Modificado la coordenada x y la alineación
ax.text(
    3.5, 2.8, "¿Qué provincias tienen más poder de 'compra compulsiva'?", 
    fontsize=20, fontweight='bold',
    ha='center', va='top'
)

# Definir una función para dibujar un solo carrito de compra
def draw_cart(x, y):
    """
    Dibujar un icono simplificado de carrito de compra en la posición (x, y)
    """
    # Cesta del carrito de compra (rectángulo)
    cart_basket = patches.Rectangle(
        (x, y), cart_width, cart_height,
        facecolor='none', edgecolor='black'
    )
    ax.add_patch(cart_basket)
    # Asa del carrito de compra (simulada por un polígono)
    cart_handle = patches.Polygon(
        [[x - 0.1, y + cart_height],
         [x + cart_width + 0.1, y + cart_height],
         [x + cart_width / 2, y + cart_height + 0.2]],
        facecolor='none', edgecolor='black'
    )
    ax.add_patch(cart_handle)
    # Ruedas del carrito de compra (dos círculos pequeños)
    wheel1 = patches.Circle((x + 0.1, y - 0.1), 0.05, color='black')
    wheel2 = patches.Circle((x + 0.2, y - 0.1), 0.05, color='black')
    ax.add_patch(wheel1)
    ax.add_patch(wheel2)

# Iterar a través de los datos para dibujar nombres de provincias + carritos de compra
for province, count in data.items():
    # Dibujar el texto de la provincia
    ax.text(
        -1.2, province_y[province] + 0.1, 
        province, fontsize=16, fontweight='bold'
    )
    # Bucle para dibujar carritos de compra
    for i in range(count):
        cart_x = 1 + i * (cart_width + 0.2)  # Espaciado horizontal entre carritos de compra
        draw_cart(cart_x, province_y[province])

plt.tight_layout()
plt.show()