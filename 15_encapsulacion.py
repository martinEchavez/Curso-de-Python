class Persona:
 #Encapsulación
 #Por defecto los atributos se declara públicos
 def __init__(self, nombre, apellido, edad):
  self.nombre = nombre #Public
  self._apellido = apellido #Protected
  self.__edad = edad #Private

 def mostrar_informacion(self):
  print(f'Nombre: {self.nombre}, Apellido: {self._apellido}, Edad: {self.__edad}')

 #GETTERS And SETTERS - Get = Obtener - Set = Cambiar un valor
 def get_edad(self):
  print(f'Obteniendo edad por método get {self.__edad}')

 def set_edad(self, edad):
  self.__edad = edad

#Instancia a la clase
persona1 = Persona('Martin', 'Echavez', '25')
persona1.__edad = '30' #No se puede modificar la edad de esta forma si este atributo es private
persona1.__edad #No se puede obtener la edad de esta forma si este atributo es private
persona1.get_edad()
persona1.mostrar_informacion()

persona2 = Persona('Juan', 'Perez', '54')
persona2._apellido = 'Fernandez' #Se puede modificar porque Protected es accecible desde la misma clase
persona2.set_edad('34') #Forma correcta de asignarle la edad a un atributo private
persona2.mostrar_informacion()