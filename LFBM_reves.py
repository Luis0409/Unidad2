
class Reves():
    
    def datos(self):
        palabra = input("Ingresa tu nombre: ")

        a = 1 
        b = len(palabra) 
        while a <= b:
            print (palabra[-a])
            a += 1 

a=Reves()
a.datos()

