import base64
import pyDes
import re


#Validación de contraseña

def validar_password(password):
  if 8 <= len(password) <= 8:
    if re.search('[a-z]', password) and re.search('[A-Z]', password):
      if re.search('[0-9]', password):
        if re.search('[!"#$%&()*+,-./:;?=@\^_`]', password):
          return True
  return False

#Seleccion de Opcion Cifrar o Descifrar
Rta = int(input("Bienvenido \n\n 1. Cifrar \n 2. Descifrar \n\n Opcion: "))
if Rta == 1:
  #Nombre del archivo con su formato    
  archivo=input("Ingrese el nombre del archivo a cifrar: ")
  #Abrir el archivo en base64
  with open(archivo, "rb") as img_file:
    b64image = base64.b64encode(img_file.read())
  #Leer la contraseña para encriptar
  key=input("Ingrese la clave: ")
  #Llamada a funcion que valida la contraseña
  validar_password(key)
  if(validar_password(key))== True:  
    #Imprimir en panralla el archivo en base64
    print("Archivo en base64:", b64image)
    #Llamada al algoritmo DES atraves de la libreria PyDes
    k = pyDes.des(key.encode(), pyDes.CBC,b"\0\1\0\1\0\1\0\0",pad=None, padmode=pyDes.PAD_PKCS5)
    #Encriptacion de el archivo generado en base64
    encriptada = k.encrypt(b64image)  
    print("Archivo cifrado: ", encriptada)
    encriptada64=base64.b64encode(encriptada)
    print("Archivo cifrado en base64: ", encriptada64)
    image = open(""+archivo, "wb")
    image.write(base64.b64decode(encriptada64))
    image.close()
    #Guarda el archivo ya encriptdado
    print("Guardado como: ",""+archivo)
  else:
    print("Tu contraseña debe integrar minusculas, mayusculas , 8 caracteres y caracteres especiales.")
else:
  #Solicita el nombre del archivo a desencriptar    
  archivo = input("Ingrese el nombre del archivo a desencriptar: ")
  #Solicita la contraseña para desencriptar
  key = input("Ingrese la contraseña: ")
  #Valida la contraseña
  validar_password(key)
  if(validar_password(key))== True: 
    #Lee el archivo en base64
    with open(archivo,"rb") as img_file:
      b64image2 = base64.b64encode(img_file.read())
    #Imprimir en panralla el archivo en base64
    print("Archivo leido en base64: ", b64image2)
    desencriptada=base64.b64decode(b64image2)
    #Utiliza la funcion de desencriptar de la libreria PyDes con el Algoritmo DES
    k=pyDes.des(key.encode(), pyDes.CBC,b"\0\1\0\1\0\1\0\0",pad=None, padmode=pyDes.PAD_PKCS5)
    desencriptada=k.decrypt(desencriptada)
    #Imprimir en panralla el archivo en base64 desencriptado
    print("Archivo descifrado en base 64: ", desencriptada)
    image=open(""+archivo,"wb")
    image.write(base64.b64decode(desencriptada))
    image.close()
    #Guarda el archivo ya desencriptado
    print("Guardado como: ", ""+archivo)
  else:
    print("Tu contraseña debe integrar minusculas, mayusculas, minimo 8 caracteres y caracteres especiales.") 