x = raw_input("ingrese una palabra combinando letras y numeros:    ")
y = len(x)
cont = 0
cont1 = 0
for i in range(0,y):
    letra = x[i]
    if letra.isdigit():
        cont = cont + 1
    if letra.isalpha():
        cont1 = cont1 + 1
print "La frase contiene",cont,"numeros"
print "La frase contiene",cont1,"letras"
