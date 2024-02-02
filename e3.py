"""
Jose Villalba Gómez
pp3
Mida de les paraules
"""
caracter = ""
mida = []*333
con = 1
pet = [[], []]
total = 0
lonMin = 200
med = total / con
while caracter != "\q":
    caracter = str(input())
    mida.insert(con, caracter)
    total = total + len(caracter)
    con = con + 1
med = total / con
for x in mida:
    if len(mida[x]) < med:
        pet[0].append(mida[x])
        pet[1].append(mida.count(mida[x]))

print("La longitud media de las palabars es: ", total/con)
print("La/s palabras de menor longitud son: ", list(zip(pet[0], pet[1])))
print(mida)

