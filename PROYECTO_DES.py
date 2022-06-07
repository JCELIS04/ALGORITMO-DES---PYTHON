import base64
import pyDes

Rta = int(input("Bienvenido \n\n 1. Cifrar \n2. Descifrar \n\n Ruta: "))
if Rta == 1:
  archivo=input("Infrgrese el nombre del archivo a cifrar: ")
  with open(archivo, "rb") as img_file:
    b64image = base64.b64encode(img_file.read())

  key=input("Ingrese la clave: ")
  print("Archivo en base64:", b64image)


  #key = "DESCRYPT"

  k = pyDes.des(key.encode(), pyDes.CBC,b"\0\1\0\1\0\1\0\0",pad=None, padmode=pyDes.PAD_PKCS5)
  encriptada = k.encrypr(b64image)

  print("Archivo cifrado: ", encriptada)
  encriptada64=base64.b64encode(encriptada)
  print("Archivo cifrado en base64: ", encriptada64)

  image = open(""+archivo, "wb")
  image.write(base64.b64decode(encriptada64))
  image.close()
  print("Guardado como: ",""+archivo)
else:
  archivo = input("Ingrese el nombre del archivo a descifrar: ")
  key = imput("Ingrese la contraseña: ")
  with open(archivo,"rb") as img_file:
    b64image2 = base64.b64encode(img_file.read())
  print("Archivo leido en base64: ", b64image2)

  desencriptada=base64.b64decode(b64image2)

  k=pyDes.des(key.encode(), pyDes.CBC,b"\0\1\0\1\0\1\0\0",pad=None, padmode=pyDes.PAD_PKCS5)
  desencriptada=k.decrypt(desencriptada)

  print("Archivo descifrado en base 64: ", desencriptada)
  image=open(""+archivo,"wb")
  image.write(base64.b64decode(desencriptada))
  image.close()
  print("Guardado como: ", ""+archivo)