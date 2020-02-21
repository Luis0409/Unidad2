class NumParImpar():

    def operacion(self):
        num = input("Ingresa un número: ")
        num = int(num)
        if num == 0 or num%2 == 0:
            print ("Numero par")
        else:
            print ("Numero impar")

dato = NumParImpar()
dato.operacion()
