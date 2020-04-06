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
  return self.__edad

 def set_edad(self, edad):
  self.__edad = edad

#La clase Ingeniero hereda de persona
class Ingeniero(Persona):
 #Se pasa el constructor
 def __init__(self, nombre, apellido, edad):
  super().__init__(nombre, apellido, edad)

ingeniero1 = Ingeniero('Jesus', 'Prazca', '26')
ingeniero1.mostrar_informacion()