def app():
 #Crear un archivo
 archivo = open('Archivo.txt', 'w') #W se usa para escribir un archivo, si no está creado lo creará
#De está forma escribimos 20 linea de código en el archivo que se acaba de crar
 for i in range(0, 20):
  archivo.write('Esta es la linea ' + str(i) + "\r\n")
 # Cerrar un archivo
 archivo.close()
app()