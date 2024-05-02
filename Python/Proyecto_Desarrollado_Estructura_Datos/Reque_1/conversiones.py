import sys

# Verificamos que se proporcionen los argumentos necesarios
if len(sys.argv) != 5:
    print("Usage: python conversiones.py <tasa_sol> <tasa_peso_arg> <tasa_dolar> <valor_en_pesos>")
    sys.exit(1)

# Convertimos los argumentos a números flotantes
try:
    tasa_sol = float(sys.argv[1])
    tasa_peso_arg = float(sys.argv[2])
    tasa_dolar = float(sys.argv[3])
    valor_en_pesos = float(sys.argv[4])
except ValueError:
    print("Error: Los argumentos deben ser números.")
    sys.exit(1)

# Realizamos las conversiones
valor_en_soles = valor_en_pesos * tasa_sol
valor_en_peso_arg = valor_en_pesos * tasa_peso_arg
valor_en_dolares = valor_en_pesos * tasa_dolar

# Imprimimos los resultados
print(f"Los {valor_en_pesos} pesos equivalen a:")
print(f"{valor_en_soles:.1f} Soles")
print(f"{valor_en_peso_arg:.1f} Pesos Argentinos")
print(f"{valor_en_dolares:.1f} Dólares")


