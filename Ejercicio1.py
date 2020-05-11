# Confeccionar un programa que lea n pares de datos, cada par de datos
#  corresponde a la medida de la base y la altura de un triángulo. El programa 
# deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12. 
valores=[]
arraySize=int(input('Num de triangulos a insertar'))
x=0
y=0
print('Programa triangulo')
for x in range(arraySize):
    base=int(input('Base: '))
    altura=int(input('altura: '))
    superficie=base*altura
    valores.append([base,altura,superficie])
    
for y in range(arraySize):
    c=y+1
    print('Triangulo ',c)
    b=valores[y][0]
    h=valores[y][1]
    s=valores[y][2]
    print('Base=',b,'\nAltura=',h,'\nSuperficie',s)