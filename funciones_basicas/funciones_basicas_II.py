#1. Cuenta regresiva: crea una función que acepte un número como entrada. 
# Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
print("N°1:cuenta regresiva")
lista=[] #lista vacía que devolverá una nueva lista
for i in range(20): #iterar i en rango del 0 al 20
    lista.append(i) #agrega el resultado de la iteracion de i a la lista
lista.reverse() #función que devuelve los valores en reversa,debe estar fuera del for,sino devuelve primero los impares en reversa y luego los pares en ascendencia
print(lista) #imprime la nueva lista


#2. Imprimir y devolver: crea una función que reciba una lista con dos números. 
# Imprime el primer valor y devuelve el segundo.
print("N°2: imprime y devuelve")
def imprimir_y_devolver(x):
    print(x[0]) #imprime el primer valor de la lista
    return(x[1]) #devuelve el segundo valor de la lista
y=imprimir_y_devolver([1,2]) 
print(y)


#Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)
print("N°3:Suma y longitud")
def suma_y_longitud(m): #crea una funcion que acepte una lista
    n=m[0]+len(m) # suma del primer valor de la lista + el largo de la lista
    return n  #devuelve el valor de la suma (guardado en n)
p=suma_y_longitud([7,2,3,4,5]) 

print(p)

#Valores mayores que el segundo: 
# escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
# Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False
print("N°4 valores mayores que el segundo")
def valores_mayores_que_el_segundo(q):
    # la lista tiene mas de 2 valores
    if len(q)<=2:
        return False
    # lista nueva 
    nueva_lista=[]
    for e in q:
        if e > q[1]:
            nueva_lista.append(e)
    # largo lista nueva
    largo=len(nueva_lista)
    print("numero de valores en lista nueva",largo)
    return (nueva_lista)

print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

#Esta longitud, ese valor:
# escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, 
# y cuyos valores sean todos el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
print("N°5:longitud y valor")
def longitud_y_valor(tamaño,valor): #funcion con dos enteros como  parametros tamaño y valor
    lista=[] #devolvera una nueva lista
    for r in range(tamaño): 
        lista.append(valor) #agrega el valor a la nueva lista
    return lista

r=longitud_y_valor(4,7)
print(r)



