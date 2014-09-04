x = raw_input("ingrese una palabra para determinar si es o no un palindromo :  ")
y = len(x)
z = ""
cont = 0
pal_inv=[]

for letras in range (0,y):
    z = x[-letras-1]
    pal_inv.append(z)
for comparar in range (0,y):
    if pal_inv[comparar] != x[comparar]:
        cont = 1
if cont == 1:
    print "no es palindromo"
else:
    print "es palindromo"
    
