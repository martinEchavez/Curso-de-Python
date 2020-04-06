#Aplicación para el manejo de una playlist
playlist = {} #Diccionario vacio
playlist['canciones'] = [] #Lista vacia de canciones

def app():
 print('***** Mi Playlist *****')
 agregar_playlist = True #Bandera para saber si se agregó un nombre

 while agregar_playlist:
  nombre_playlist = input('Ingresa el nombre de la playlist: ')
  if nombre_playlist:
   playlist['nombre'] = nombre_playlist
   agregar_playlist = False #Pasa a ser False cuando se agrega el nombre
   agregar_canciones()

def agregar_canciones():
 agregar_cancion = True #Bandera para agregar canción
 while agregar_cancion:
  nombre_playlist = playlist['nombre']
  pregunta = f'\r\nAgrega caciones a la playlist {nombre_playlist}\r\n'
  pregunta += 'Escribe X para salir\r\n'
  cancion = input(pregunta)
  if cancion == 'X':
   #Dejar de agregar canciones
   mostrar_resumen()
   agregar_cancion = False
  else:
   playlist['canciones'].append(cancion)
   print(playlist)

def mostrar_resumen():
 nombre_playlist = playlist['nombre']
 print(f'*** {nombre_playlist} ***')
 print('Canciones')
 for cancion in playlist['canciones']:
  print(f'- {cancion}')

app()