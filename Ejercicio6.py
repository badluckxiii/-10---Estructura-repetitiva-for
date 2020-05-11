# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos 
# en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto 
# cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos 
# a procesar
ncoordenadas=[]
print('Clasificacion de coordenadas por cuadrantes')
numcoordenadas=int(input('Numero de coordenadas a insertar'))
for interador in range(numcoordenadas):
    x=int(input('Coordenada x: '))
    y=int(input('Coordenada y: '))
    ncoordenadas.append([x,y])
pcuadrante=0
scuadrante=0
tcuadrante=0
qcuadrante=0
z=0
for z in range(len(ncoordenadas)):
    
    x=ncoordenadas[z][0]
    y=ncoordenadas[z][1]
    print('Coordenada x:',x,'Coordenada y:',y)
    if(x>0 and y>0):
        pcuadrante+=1
    elif(x<0 and y>0):
        scuadrante+=1
    elif (x<0 and y<0):
        tcuadrante+=1
    elif (x>0 and y<0):
        qcuadrante+=1
print('Coordenadas primer cuadrante',pcuadrante,
'\nCoordenadas segundo cuadrante',scuadrante,
'\nCoordenadas tercero cuadrante',tcuadrante,
'\nCoordenadas cuarto cuadrante',qcuadrante)