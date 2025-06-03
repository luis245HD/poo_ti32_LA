#Alcance de las variables
#tipo de dato string
class Variables:
        texto:str = "None"
        def __init__(self,cadena:str , ):
                self.cadena=cadena
                
        #Metodo constructor  
        def contarCaracteres(self, texto:str)-> None:
                print(len(texto))
                print(len(self.cadena ))
                print(len(self.texto))

        
        def caracter(self,posicion:int)-> None:
             print(self.cadena[posicion])

mi_objeto= Variables("adios")
mi_objeto.contarCaracteres("hola")
#llamada al metodo caracter para mostr
mi_objeto.caracter(3)