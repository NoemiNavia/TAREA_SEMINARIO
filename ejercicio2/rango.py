x = input("ingrese un # de inicio del rango:  ")
y = input("ingrese un # de fin de rango:  ")
lista = []
if x < y:
    print "lista de numeros de",x,"a", y
    for i in range(0,y-x+1):
        lista.append(i+x)
        
    for i in range(0,y-x+1):
        print lista[i]
    print "lista de numeros pares"    
    for i in range(0,y-x+1):
        if lista[i]%2==0:
            print lista[i]
else :
    print "El inicio del rango es mayor al numero final del rango"
    print "o simplemente no introdujo un numero valido"
            
