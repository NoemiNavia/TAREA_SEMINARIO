import math

print ("INGRESE TRES NUMEROS PARA SABER SI ES UN TRIANGULO")
x = input("ingrese el primer numero :  ")
y = input("ingrese el segundo numero :  ")
z = input("ingrese el tercer numero:  ")
equi = 0
def triangulo(x1,y1,z1):
    if x1==y1 and y1==z1:
        print "es un triangulo equilatero"
    if (x1==y1 and y1!=z1)or(x1==z1 and z1!=y1)or(y1==z1 and z1 !=x1):
        print "Es un triangulo isósceles"
    if x1>y1:
        if x1>z1:
            equi = math.sqrt(pow(y1,2)+pow(z1,2))
            if equi == x1:
                print "Es un triangulo rectangulo"
            else:
                if x1>(z1+y1):
                    print x1
                    print "No es un trinagulo : uno de los lados no es correcta"
        else:
            equi = math.sqrt(pow(x1,2)+pow(y1,2))
            if equi == z1:
                print "Es un triangulo rectanguloo"
            else:
                if z1>(x1+y1):
                    print z1
                    print "No es un trinagulo : uno de los lados no es correcta"
    if y1 > z1:
        equi = math.sqrt(pow(x1,2)+pow(z1,2))
        if equi == y1:
            print "Es un triangulo rectangulo"
        else:
            if y1>(z1+y1):
                print y1
                print "No es un trinagulo : uno de los lados no es correcta"
    if x1!=y1 and y1!=z1:
        print "Es un triangulo escaleno"
        
triangulo(x,y,z)
