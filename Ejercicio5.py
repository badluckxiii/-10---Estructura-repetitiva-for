# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales)
# , isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo
print('Classificació de triangles')
ntriangles=[]
numt=int(input())
for x in range(numt):
    a=int(input('Costat 1:'))
    b=int(input('Costat 2:'))
    c=int(input('Costat 3:'))
    ntriangles.append([a,b,c])
nequilateros=0
nisosceles=0
nescaleno=0
for y in range(len(ntriangles)):
    c1=ntriangles[y][0]
    c2=ntriangles[y][1]
    c3=ntriangles[y][2]
    if c1==c2 and c2==c3:
        nequilateros+=1
    elif c1==c2 or c1==c3 and c2!=c3:
        nisosceles+=1
    elif c1!=c2 and c2!=c3:
        nescaleno+=1
print('equilátero',nequilateros,'isósceles',nisosceles, 'escaleno',nescaleno
)