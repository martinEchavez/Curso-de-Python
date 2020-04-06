#Realiza un examén con 3 preguntas, el usuario debería responder SI o NO y al final
#otorgarle una calificación
#la calificación se logra con una variable que inicie en 0 y por cada respuesta correcta incremente un 1
print('Bienvenido al examen')
contador = 0

pregunta1 = input('¿9 es un número primo?: ')
if pregunta1 == 'Si':
 contador += 1
pregunta2 = input('¿10 es un número par?: ')
if pregunta2 == 'Si':
 contador += 1
pregunta3 = input('¿0 es un número primo?: ')
if pregunta3 == 'Si':
 contador += 1

print(f'El resultado es: {contador}')