
#Verificar si ambas variables cambian 

a = b = [1, 2, 3]

a.append(4)

if a != b:
    print("No genero cambios")
elif a == b:
    print("Si hubo cambios")
    print(a, b)  #HUBO CAMBIOS PQ LA MISMA LISTA OCURRE PARA AMBOS A Y B 
else:
    print("error")

