print("Hola esto es una prueba\n")

lista = range(100) # range(a,b) [a,b]
print(list(lista))

x = list(range(1,11,2))

# for i in range(len(x)):
# print(i, x[i]) 

# for i, elemento in enumerante(x):
#     print (i,elemento)

import random

desordenada = [random.randint(1,100)for _ in range(10)]

desordenada.sort()
print(desordenada)
desordenada.sort(reverse=True)
print(desordenada)

otralista= list('Marco cordero')
elemento = otralista[0] + otralista[1] + otralista[2] + otralista[3] #Mar
elemento = otralista[0:4] #Marc
elemento = otralista [4:] #
elemento = otralista [:4] #Marc
#elemento = otralista [0:-4:3] # Toma los caracteres de 3 en 3
#elemento = otralista [::-1] #El nombre al reves

elemento.reverse()
print(elemento)# otra reversa

holder = ''
for i in range (len(otralista)):
    holder= otralista[i] + holder
print(holder)

lista = list(range(10))
print(lista[len(lista)-1])
print(lista)
# holder = list.pop()#cuando esta vacio toma el ultimo elemento
print(holder)
print(lista)

listavacia = []
for i in range(50):
    listavacia.append(i+1)
print(listavacia) #llena una lista vacia del 1 al 50

# x = [0,1,2,3,4,5,6]
# x.remove[1, true]#remueve el elementp de la posiscion 1
# print(x)

y = [0,1,2,3,4,5,6]
y.insert(-2,True)
print(y)


