# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre 
# la tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, 
# hasta el 36. 
tmultiplicar=int(input('Tabla de multiplicar'))
print('Tabla de multiplicar del ',tmultiplicar)
for x in range(13):
    if x!=0:
        print(tmultiplicar,'x',x,'=',tmultiplicar*x)