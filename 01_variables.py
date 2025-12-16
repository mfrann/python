

### Variables ###

my_str = "My String variable"
print(my_str)

my_int = 5
print(my_int)

my_int_str = str(my_int)
print(my_int_str)
print(type(my_int_str))

my_bool = False
print(my_bool)

# Concatenación de variables en un print
print(my_str, my_int_str, my_bool)
print("Este es el valor de:", my_bool)

# Algunas funciones del sistema
print(len(my_str)) #leer los caracteres

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Martin", "Caycho", 'iFran', 18
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 18
age = "Fran"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección" #IMPRIMIRA TIPO STRING
address = True
address = 5
address = 1.2
print(type(address))