lista_1=['uno','dos','tres','cuatro']
listaNumerica=[]
indice=0
positivos=int(0)
negativos=int(0)
mayores=int(0)
#dato=int(0)
while (indice <= 5):
  dato=int(input('ingrese numero entero: '))
  listaNumerica.append(dato)
  indice +=1 
print(listaNumerica)

for dato in listaNumerica:
  if (dato >= 0):
    positivos+=1
  else:
     negativos+=1
print ('Numeros Positivos: ', positivos)
print ('Numeros Negativos: ', negativos)
print ('Numeros Mayores a 100: ', mayores)
 
