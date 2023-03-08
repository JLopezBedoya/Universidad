print("Punto 6")
array = [1,2,2,5,4,6,7,8,8,8]
conc = 0
cont = 0
for i in range (10):
    for l in range(len(array)):
        if i == array[l]:
            conc+=1
    if conc>cont:
        cont = conc
        max = i
    conc = 0
print(f"longest: {cont}")
print(f"Number: {max}")