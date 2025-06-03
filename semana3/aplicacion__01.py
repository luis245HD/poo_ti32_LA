class Calculadora:

    def __init__(self):
     print("constructor")
    
    def sumar(self, numero1, numero2):
        #Recibe dos valores y los suma y los almacena en resultado
        resultado = numero1 + numero2
       
        #Imprime el texto resultado y el valor de la variable  resultado
        #convierte el tipo de dato a string
        print(f" resultado:" + str(resultado))

        #Imprime el texto resultado y el valor de la variable  resultado
        print(f" resultado: {resultado}")
 #Crea una instancia de la clase Calculadora, es decir crea un objeto        
mi_objeto = Calculadora()
#Invoca al metodo sumar y le envia 2 numeros 
mi_objeto.sumar(5, 10)
#Invoca al metodo sumar y le envia 2 cadenas 
mi_objeto.sumar("hola", "adios")


