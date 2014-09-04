print ("TABLA DE DIVISION DEL 1 AL 10")
indice = 1
cont = 0
while indice <= 10:
    print "TABLA DE DIVISION DE",indice
    for i in range (0,10):
        cont = cont + indice
        print cont, "\t/\t" ,indice, "\t=\t", cont/indice
    cont = 0
    indice = indice +1   
        
