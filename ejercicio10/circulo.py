from math import pi
class circulo():
    
    def darArea(self,rad):
        area = pow(rad,2)* pi
        print "El area del circulo introducido es:  ", area
objeto = circulo()
x = input("Ingrese un mumero representando un radio de un circulo : ")
objeto.darArea(x)
