# --- Tasa de cambio (1 MXN equivale a:) ---
# Valores de referencia aproximados
USD_TASA = 0.049    # Dólar Estadounidense
EUR_TASA = 0.047    # Euro
THB_TASA = 1.66     # Baht Tailandés
JPY_TASA = 7.52     # Yen Japonés
KRW_TASA = 69.30    # Won Surcoreano
AUD_TASA = 0.076    # Dólar Australiano
PEN_TASA = 0.19     # Sol Peruano
CAD_TASA = 0.069    # Dólar Canadiense
VES_TASA = 1.76     # Bolívar Venezolano
ARS_TASA = 48.90    # Peso Argentino

# 1. Solicitamos la cantidad en Pesos Mexicanos
pesos_mxn = float(input("Introduce la cantidad en Pesos Mexicanos (MXN): $"))

# 2. Mostramos el menú de opciones al usuario
print("\n--- MENÚ DE CONVERSIÓN DE DIVISAS ---")
print("1. Dólar (USD)")
print("2. Euro (EUR)")
print("3. Baht (THB)")
print("4. Yen (JPY)")
print("5. Won (KRW)")
print("6. Dólar Australiano (AUD)")
print("7. Sol (PEN)")
print("8. Dólar Canadiense (CAD)")
print("9. Bolívar (VES)")
print("10. Peso Argentino (ARS)")
opcion = int(input("\nSelecciona el número de la moneda de destino (1 - 10): "))

# Variables para almacenar el resultado y el nombre de la divisa
convertido = 0.0
moneda = ""

# 3. Estructura match-case para realizar el cálculo según la opción
match opcion:
    case 1:
        convertido = pesos_mxn * USD_TASA
        moneda = "USD (Dólares)"
    case 2:
        convertido = pesos_mxn * EUR_TASA
        moneda = "EUR (Euros)"
    case 3:
        convertido = pesos_mxn * THB_TASA
        moneda = "THB (Bahts)"
    case 4:
        convertido = pesos_mxn * JPY_TASA
        moneda = "JPY (Yenes)"
    case 5:
        convertido = pesos_mxn * KRW_TASA
        moneda = "KRW (Wons)"
    case 6:
        convertido = pesos_mxn * AUD_TASA
        moneda = "AUD (Dólares Australianos)"
    case 7:
        convertido = pesos_mxn * PEN_TASA
        moneda = "PEN (Soles)"
    case 8:
        convertido = pesos_mxn * CAD_TASA
        moneda = "CAD (Dólares Canadienses)"
    case 9:
        convertido = pesos_mxn * VES_TASA
        moneda = "VES (Bolívares)"
    case 10:
        convertido = pesos_mxn * ARS_TASA
        moneda = "ARS (Pesos Argentinos)"
    case _:
        moneda = "Invalida"

# 4. Imprimir el resultado final
if moneda == "Invalida":
    print("\n X Error: Opción no válida. Debes elegir un número del 1 al 10.")
else:
    print(f"\n${pesos_mxn:.2f} MXN equivalen a: {convertido:.2f} {moneda}")