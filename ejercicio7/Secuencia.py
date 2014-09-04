x = input("Ingrese un numero : ")
cont = (x*2)-1
i=1
n = 1
while n<=cont:
    if n<=x:
        for i in range(0,n):
            print n,
    if n==x: print ""        
    if n>=x:
        for i in range(n,cont):
            print cont-n,
    print 
    n=n+1
