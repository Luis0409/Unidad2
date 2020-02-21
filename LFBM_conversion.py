
class conversionFC:

    def conversion(self):
        cel = int(input('Ingresa la Temperatura en Grados cel: '))
        fah = 9.0/5.0 * cel +32
        print('{}°C Equivale a {}°F'.format(cel, fah))

        fah = int(input('Ingresa la Temperatura en Grados fah: '))
        cel = (fah -32 ) * 5.0/9.0
        print ('{}°F Equivale a {}°C'.format(fah, cel))

f = conversionFC()
f.conversion()
