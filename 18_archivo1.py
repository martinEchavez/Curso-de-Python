def app():
#No se le pasa párametro porque por defecto viene en lectura
 with open('Archivo.txt') as archivo:
  for contenido in archivo:
   print(contenido.rstrip())#rstrip Elimina los espacios en blanco

app()