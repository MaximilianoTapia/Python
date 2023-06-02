#EJERCICIO UNO
for x in range(0, 151, 1):
    print(x)

#EJERCICIO DOS
for x in range(5, 1001, 5):
    print(x)

#EJERCICIO TRES
for x in range(1,101):

    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#EJERCICIO CUATRO
suma = 0

for x in range(1,500001):
    suma += x

print(suma)

#EJERCICIO CINCO

for x in range(2018,1,-4):
    print(x)
    
#EJERCICIO SEIS
low = 2
high = 9
mult = 3

for x in range (low,high,1):

    if x % mult == 0:
        print(x)