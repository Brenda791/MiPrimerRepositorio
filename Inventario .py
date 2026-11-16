# 1. Crear el diccionario del inventario de productos
inventario = {
    "PROD001": {"nombre": "Laptop", "precio": 899.99, "stock": 10},
    "PROD002": {"nombre": "Mouse inalámbrico", "precio": 25.50, "stock": 3},
    "PROD003": {"nombre": "Monitor 4K", "precio": 349.99, "stock": 6},
    "PROD004": {"nombre": "Teclado mecánico", "precio": 79.99, "stock": 2},
    "PROD005": {"nombre": "Auriculares Gamer", "precio": 120.00, "stock": 15}
}

# 2. Calcular el valor total del inventario
valor_total = sum(item["precio"] * item["stock"] for item in inventario.values())

# 3. Encontrar el producto más caro y el más barato
# Usamos el parámetro 'key' para comparar por el campo 'precio'
prod_mas_caro = max(inventario.values(), key=lambda x: x["precio"])
prod_mas_barato = min(inventario.values(), key=lambda x: x["precio"])

# 4. Filtrar productos con stock bajo (menos de 5 unidades)
stock_bajo = [item["nombre"] for item in inventario.values() if item["stock"] < 5]

# --- Mostrar los resultados en consola ---
print(f"Valor total del inventario: ${valor_total:,.2f}\n")

print(f"Producto más caro: {prod_mas_caro['nombre']} (${prod_mas_caro['precio']})")
print(f"Producto más barato: {prod_mas_barato['nombre']} (${prod_mas_barato['precio']})\n")

print("Productos con stock bajo (menos de 5 unidades):")
for prod in stock_bajo:
    print(f"  - {prod}")