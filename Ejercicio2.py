#Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
suma=0
r=[]
# x=0
print('Programa per a sumar ultims 5 numeros')
for x in range(10):
    c=x+1
    print('Valor ',c)
    valor=int(input('Valor: '))
    r.append(valor)
for y in range(len(r)):
    if(y>4):
        suma+=r[y]
print('Suma ultims numeros ',suma)
