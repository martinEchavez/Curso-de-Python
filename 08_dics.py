#Diccionarios
persona = {
 'nombre': 'Martin', #Clave valor
 'apellido' : 'Echavez',
 'ocupacion' : 'Estudiante',
 'edad': 25,
 'activo' : True
}
print(persona)
#Acceder a los elementos
print(persona['nombre'])
#Eliminar un valor
del persona['ocupacion']
print(persona)
#Accediendo a los valores con get ('valor', 'mensaje en caso que no se encuentre ese valor')
print(persona.get('apellido', 'No existe ese valor'))
print(persona.get('estado_civil', 'No existe ese valor'))
#Recorrer un diccionario
for llave, valor in persona.items():
 print(llave,' : ', valor)