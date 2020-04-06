precio = 5000
if precio > 5500:
 print('hay descuento')
else:
 print('No hay descuento')

#Negación de un If !=
if not precio == 5100:
 print('El precio es diferente de 5000')

#Boolean con negación
usuario_autenticado = True
if not usuario_autenticado:
 print('Debes iniciar sesión')
else:
 print('Bienvenido')

lenguajes = ['Python', 'Java', 'JavaScript']
#Evaluar elementos de una lista
if 'Java' in lenguajes:
 print('Java si existe')

#Operadores anidados AND OR
usuario_autenticado = True
usuario_admin = True
if usuario_autenticado and usuario_admin:
 print('acceso total..')
else:
 print('No tiene permiso')