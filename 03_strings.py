

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string)) #Longitud de la variable
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Martin", "Caycho", 18
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language #Separa cada caracter
print(a)
print(e)

# División

language_slice = language[1:3] #Empieza en el indice 1 y va hasta el 3 pero sin incluirlo
print(language_slice)

language_slice = language[1:] #Empieza en el indice 1 y va hasta el final
print(language_slice)

language_slice = language[-2] #Empieza en el indice -2 y va hasta el final
print(language_slice)

language_slice = language[0:6:2] #Empieza en 0 hasta el 6 y va de 2 en 2
print(language_slice)

# Reverse

reversed_language = language[::-1] #Empieza desde el final hasta el principio
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) #Primera letra mayuscula
print(language.upper()) #Todo mayuscula
print(language.count("t")) #Contar letras
print(language.isnumeric()) #?Es numerico
print("1".isnumeric())
print(language.lower()) #Todo minuscula
print(language.lower().isupper()) #?Es mayuscula
print(language.startswith("Py")) #Empieza con Py
print(language.startswith("py")) #empieza con py
print("Py" == "py")  # No es lo mismo