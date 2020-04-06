lenguajes = ['Python', 'Java', 'JavaScript']
#Método para ordenar una lista
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de una lista
#La f se utiliza para mezclar un String con una variable
aprendiendo = f'Estoy aprendiendo {lenguajes[1]}'
print(aprendiendo)

#Modificar una Lista
lenguajes[2] = 'Kotlin'
print(lenguajes)

#Agregar elementos a una lista
lenguajes.append('php')
print(lenguajes)

#Eliminar un elemento de la lista
#del = delete
del lenguajes[1]
print(lenguajes)

#Eliminar el último elemento
lenguajes.pop()
print(lenguajes)

#Eliminar por indice en la lista
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('Kotlin')
print(lenguajes)