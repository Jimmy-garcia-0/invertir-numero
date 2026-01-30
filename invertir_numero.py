# Entrada
n = int(input("Introduce un número de 4 dígitos: "))

# Extraemos los dígitos de forma independiente
d1 = n % 10    * 1000      # Unidad
d2 = n // 10 % 10   * 100  # Decena
d3 = n // 100 % 10   * 10 # Centena
d4 = n // 1000       # Millar

# Inversion
invertido =d1+d2+d3+d4
# Salida
print("El número invertido es:", invertido)








