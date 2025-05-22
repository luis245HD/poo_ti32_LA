class Mayor:
     
    def __init__(self):
        
      pass
        
    def mayor(self, numero1:int, numero2:int, numero3:int)-> None:
       if numero1>=numero2 and numero1>=numero3:
              print(f"El mayor es: {numero1}")
       elif numero2>=numero1 and numero2>=numero3:
              print(f"El mayor es: {numero2}")
       else:
           print(f"El mayor es: {numero3}")
         
mi_objeto = Mayor()
mi_objeto.mayor(1, 2, 3)
mi_objeto.mayor(1, 3, 2)
mi_objeto.mayor(3, 1, 2)
mi_objeto.mayor(3, 1, 1)
mi_objeto.mayor(1, 1, 3)
mi_objeto.mayor(1, 3, 1)
mi_objeto.mayor(2, 1, 3)
mi_objeto.mayor(3, 1, 3)
mi_objeto.mayor(1, 3, 3)
mi_objeto.mayor(3, 3, 3)




    