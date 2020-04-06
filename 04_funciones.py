def mostar_nombre():
 print('Martin Elias')

mostar_nombre()

#Funciones con parametros
def informacion(nombre, genero):
 print(f'Mi nombre es {nombre} y soy de genero {genero}')

informacion('Juan Ramires', 'Masculino')
informacion('Alicia Campos', 'Femenina')

#Funciones con parametros por defecto
def informacion_personas(nombre, genero = 'Otro'):
 print(f'Mi nombre es {nombre} y soy de genero {genero}')

informacion_personas('Juan Ramires', 'Masculino')
informacion_personas('Alicia Campos')

#Funciones que retornan un valor
def persona(nombre):
 return nombre

persona1 = persona('Martin')
print(persona1)

def suma(a,b):
 return a + b

resultado = suma(4, 3)
print(resultado)

#Funciones VS métodos
nombre = 'Martin'
def mostrar_nombre(nombre):
 print(f'Hola {nombre}')

mostrar_nombre(nombre)

#Métodos
print(nombre.upper())