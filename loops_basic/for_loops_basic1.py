#Básico: imprime todos los números enteros del 0 al 150.
print("Números del 0 al 150")
for i in range(151):
    print(i)

#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for i in range(5,1001,5):
    print(i)

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for (i) in range(101): 
    if i % 5==0:
        print("Coding")
    else:
        print(i)
    if i % 10==0:
        print("Coding Dojo")


#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
x=0

for i in range(0, int(500.000)):
    if i % 2 !=0:
        print(i)
        x=x+i
print("La suma final es"  ,x)


#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for i in range(2018,0 , -4):
    print(i)


#Contador flexible: establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, 
# imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).
lowNum=1
highNum=20
mult=2

for i in range(lowNum, highNum+1):
    if i % mult== 0:
        print(i,end=", ")