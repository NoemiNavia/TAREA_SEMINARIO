print "Numeros primos"
y = input("Ingrese un numero :  ");
cont = 0
acum = 0
nu = y * 3
lista = []
def num_primos(nu):
    acum = 0
    for n in range(2, nu):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            cont = n
            lista.append(cont)
    for i in range (0,y):
        acum = acum + lista[i]
    print "La suma de los numeros primos es :  ",acum
            
        
num_primos(nu)
