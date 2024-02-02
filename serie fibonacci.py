def fact (n:int)-> int:
    if (n == 0):
        return 1
    return n * fact(n -1)
print(fact(5))


def fib(n): #definimos la funcion con (n)
    if n >= 0: #si el valor de n es mayor o igual a cero entonces. . .
        print("tabla(", n, ") = ", fib1(n)) #la función devuelve el valor del n
        fib(n - 1) #a esto se lo conoce  recursiva  fibona(n - 1) se llama a sí misma con n - 1 como argumento. 
                   #esto significa que la función se ejecutará nuevamente

def fib1(n): #definimos otra funcion
    if n in (0, 1): #si n es 0 o 1, la función devuelve directamente el valor de n, esto maneja los casos base de la serie
        return n #si n es igual a 0 o 1 
    else:
        return fib1(n - 1) + fib1(n - 2)#Si "n" no es 0 ni 1, entonces el valor de fibonacci para n es la suma de los valores

numero = int(input("Ingrese un número para generar la serie : "))#Se ingresa el numero 

print(f"Serie {numero} números:") #imprime la serie y hacemos llamar la variable con un operador 
fib(numero)
