### Tuples ###
#Las tuplas son unmutables, es decir, no se pueden modificar una vez creadas.
#Se puede utilizar para proteger datos que no deben cambiarse. 

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (18, 1.65, "Martin", "Caycho", "Martin", "Martin")
print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])
# my_tuple[0] = 20 TypeError: 'tuple' object does not support item assignment


print(f'Hay {my_tuple.count("Martin")} Martin en la tupla')
print(my_tuple.index("Martin")) #Se queda con el primero índice que encuentra
