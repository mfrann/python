

### Lists ###

# Definición

my_list = list() #Lista vacia
my_other_list = [] #Lista vacia

print(len(my_list)) #Cantidad de elementos en la lista 

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [18, 1.65, "Martin", "Caycho"]

print(type(my_list)) #LIST
print(type(my_other_list)) #LIST

# Acceso ]a elementos y búsqueda

print(my_other_list[0]) #PRIMER ELEMENTO
print(my_other_list[1]) #SEGUNDO ELEMENTO
print(my_other_list[-1]) #ULTIMO ELEMENTO
print(my_other_list[-4]) #PRIMER ELEMENTO
print(my_list.count(30)) #CUENTA CUANTOS ELEMENTOS DE ESE VALOR HAY EN LA LISTA
# print(my_other_list[4) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Martin")) #INDICE DEL ELEMENTO

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("iFran") #CREA EL ELEMENTO AL FINAL DE LA LISTA
print(my_other_list)

my_other_list.insert(1, "Rojo") #CREA EL ELEMENTO EN LA POSICION INDICADA 
print(my_other_list)

my_other_list[1] = "Azul" 
print(my_other_list)

my_other_list.remove("Azul") #ELIMINA EL ELEMENTO INDICADO
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop()) #ELIMINA EL ULTIMO ELEMENTO Y LO DEVUELVE
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() #ORDENA LA LISTA DE MENOR A MAYOR
print(my_new_list)

# Sublistas

print(my_new_list[1:3]) #DESDE EL INDICE 1 HASTA EL 3 PERO SIN INCLUIRLO 

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))