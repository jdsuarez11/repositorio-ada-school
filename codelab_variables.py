# Definir una variable para cada tipo de primitivo
variable_string = "Azul"
variable_int = 6
variable_float = 1.10
variable_bool = True

# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
variable_concatenar = variable_string + " " + str(variable_int) + " " + str(variable_float) + " " + str(variable_bool)

# Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
# Maximum and minimum values for integer and float data types: Max Int: 9223372036854775807 Min Int: -9223372036854775808 Max Float: 1.7976931348623157e+308 Min Float: 2.2250738585072014e-308

# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
suma_pares = variable_int * (2 + variable_int) / 2

# Imprimir los resultados de las tareas anteriores
print(variable_concatenar)
print(suma_pares)