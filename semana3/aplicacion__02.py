class Calculadora:

    def __init__(self):
       #Indica que paso por esta linea y  que  se ejecuto la siguiente linea
       pass
      
    def sumar(self, numero1:int, numero2:int):
        resultado = numero1 + numero2
        print(f"Resultado: {resultado}")

    def restar(self, numero1, numero2):
        resultado = numero1 - numero2
        return resultado
    
    def multiplicar(self, numero1, numero2):
        resultado = numero1 * numero2
        return resultado
    
    def dividir(self, dividendo:int, divisor:int):
        try:
             resultado = dividendo / divisor
             print(resultado)
        except ZeroDivisionError as error:
             print(f"Error : {error.args[0]}")
        except TypeError as error:
             print(f"Error : {error.args[0]}")
        except Exception as error:
             print(f"Error 003  : {error.args[0]}")
    

mi_objeto = Calculadora()
mi_objeto.sumar(5, 10)
print(f"Resultado: {mi_objeto.restar(10,5)}")
print(f"Resultado: {mi_objeto.multiplicar(10,5)}")
print(f"Resultado: {mi_objeto.dividir(10,5)}")
mi_objeto.dividir(divisor=20,divdendo=10)
