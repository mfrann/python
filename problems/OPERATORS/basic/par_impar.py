
num = int(input("Hasta que numero quieres generar: "))

for i in range(0, num+1):
    if i % 2 == 0:
        print(f'{i} es PAR')
    else:
        print(f'{i} es IMPAR') 
    
    i += 1

    