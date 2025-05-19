class Calculadora:

    def __init__(self):
     print("constructor")
    
    def sumar(self, numero1, numero2):
        resultado = numero1 + numero2
        print(f" resultado:" + str(resultado))
        
mi_objeto = Calculadora()
mi_objeto.sumar(5, 10)
mi_objeto.sumar("hola", "adios")

