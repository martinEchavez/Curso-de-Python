class Persona:
 #Cosntructor se inicializa o se llama de automaticamente
 #Abstración datos necesarios para 'Construir' una persona
 def __init__(self, nombre, apellido, edad):
  self.nombre = nombre
  self.apellido = apellido
  self.edad = edad

 def mostrar_informacion(self):
  print(f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}')
#Instancia a la clase
persona1 = Persona('Martin', 'Echavez', '25')
persona1.mostrar_informacion()

persona2 = Persona('Juan', 'Perez', '54')
persona2.mostrar_informacion()