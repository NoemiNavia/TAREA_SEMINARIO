x = raw_input("Ingrese la primera palabra :  ")
y = raw_input("Ingrese la segunda palabra :  ")

def valorCadena(x1,y1):
    pal1 = len(x1)
    pal2 = len(y1)
    if pal1 > pal2:
        print "La palabra",x1," tiene mayor longitud"
    if pal2 > pal1:
        print "La palabra",y1," tiene mayor longitud"
    if pal1 == pal2:
        print "Las 2 palabras tienen la misma longitud","'",(x1+y1),"'"
valorCadena(x,y)
