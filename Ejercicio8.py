# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos
#  tiene un promedio de edades mayor. 
print('Clasificar promedio edades por turnos')
edadmanana=0
edadtarde=0
edadnoche=0
vmanana=[]
vtarde=[]
vnoche=[]
promedioManana=0
promedioTarde=0
promedioNoche=0
print('Edades turno mañana')
for x in range(5):
    edad=int(input('Edades: '))
    vmanana.append(edad)
print('Edades turno tarde')
for x in range(6):
    edad=int(input('Edades: '))
    vtarde.append(edad)
print('Edades turno noche')
for x in range(11):
    edad=int(input('Edades: '))
    vnoche.append(edad)
print('Edades turno mañana')
for x in range(len(vmanana)):
    edadManana=vmanana[x]
    print('Edad: ',edadManana)
    if(x==len(vmanana)-1):
        promediomanana=edadManana/len(vmanana)

print('Edades turno tarde')
for x in range(len(vtarde)):
    edadtarde=vtarde[x]
    print('Edad:',edadtarde)
    if(x==len(vtarde)-1):
        promedioTarde=edadtarde/len(vtarde)
print('Edades turno noche')
for x in range(len(vnoche)):
    edadnoche  =vnoche[x]
    print('Edad:',edadnoche)
    if(x==len(vnoche)-1):
        promedioNoche=edadnoche/len(vnoche)
print('Promedio manana:',promediomanana,
'\npromedio tarde',promedioTarde,
'\npromedio noche',promedioNoche,
)
    