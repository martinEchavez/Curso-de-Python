class Persona:
 #Encapsulación
 #Por defecto los atributos se declara públicos
 def __init__(self, nombre, apellido, edad):
  self.nombre = nombre #Public
  self._apellido = apellido #Protected
  self.edad = edad

 def mostrar_informacion(self):
  print(f'Nombre: {self.nombre}, Apellido: {self._apellido}, Edad: {self.edad}')

 #GETTERS And SETTERS - Get = Obtener - Set = Cambiar un valor
 def get_edad(self):
  return self.edad

 def set_edad(self, edad):
  self.edad = edad

#La clase Ingeniero hereda de persona
#Este es un ejemplo de polimorfismo básico
class Ingeniero(Persona):
 #Se pasa el constructor
 def __init__(self, nombre, apellido, edad, titulado):
  super().__init__(nombre, apellido, edad)
  self.titulado = titulado #Se agrega el atributo titulado, para saber si ya está titulado o no
#Sobreescribiendo un método
 def mostrar_informacion(self):
  print(f'Nombre: {self.nombre}, Apellido: {self._apellido}, Edad: {self.edad}, titulado:  {self.titulado}')

 def get_titulado(self):
  return self.titulado

ingeniero1 = Ingeniero('Jesus', 'Prazca', '26', True)
ingeniero1.mostrar_informacion()
titulado = ingeniero1.get_titulado()
if(titulado):
 titulado = 'Si'
else:
 titulado = 'No'

print(f'Está titulado? {titulado}')
