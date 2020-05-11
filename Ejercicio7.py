# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares. 
valor=[]
for x in range(10):
    v=int(input('Valor de x: '))
    valor.append(v)
menor=0
mayor=0
multiplequinze=0
mutipledos=0
suma=0
for y in range(len(valor)):
    if(valor[y]<0):
        menor=+1
    if(valor[y]>0):
        mayor=+1        
    if(valor[y]%15==0):
        multiplequinze=+1
    if(valor[y]%2==0):
        suma+=valor[y]
        mutipledos=+1
print('Menor de 0:',menor,'\nMayor de 0: ',mayor,
'\nMultiples de 15: ',multiplequinze,'\nMultiples de 2 suma: ',suma)

