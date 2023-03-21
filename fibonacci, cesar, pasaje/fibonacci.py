import random
l = int(input("Ingrese el limite de la secuencia fibonacci: "))
a = random.randint(1,10)
b = random.randint(1,10)
fibo = [a, b]
for i in range (2, l):
    nacci = fibo[i-1]+fibo[i-2]
    fibo.append(nacci)
print(fibo)
    