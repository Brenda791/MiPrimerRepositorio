# Solicitar el precio original al usuario y lo convertira decimal
precio_original = float(input("Introduce el precio original del producto: "))

# Determinamos el porcentaje de descuento ordenando de mayor a menor precio
if precio_original > 500:
    descuento = 0.25  # 25%
elif precio_original > 200:
    descuento = 0.20  # 20%
elif precio_original > 100:
    descuento = 0.10  # 10%
else:
    descuento = 0.00  # Sin descuento

# Calculamos el monto a descontar y el precio final
monto_descuento = precio_original * descuento
precio_final = precio_original - monto_descuento

# Mostramos los resultados en pantalla con dos decimales
print(f"Descuento aplicado: {descuento * 100:.0f}% (${monto_descuento:.2f})")
print(f"El precio final es: ${precio_final:.2f}")