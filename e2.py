"""
Jose Villalba Gómez
pp3
PARAULES amb Números
Programa que lee frases por tecladp y cambia las vocales por números.
"""
try:
    frase = str(input())
    vocal = ["a","e","i","o","u"]

    while frase != "eso es todo amigos":
        frase = list(str(input()))
        for x in range(0, len(frase)):
            if frase[x] in vocal:
                match frase[x]:
                    case "a", "á", "à":
                        frase.insert(x, "1")

                    case "e", "é", "è":
                        frase.insert(x, "2")

                    case  "i", "í", "ì":
                        frase.insert(x, "3")

                    case "o", "ó", "ò":
                        frase.insert(x, "4")

                    case "u", "ú", "ù":
                        frase.insert(x, "5")
                    case _:
                        frase[x] == frase[x]

        frase = str(input())
except ValueError:
    print("No has introducido una frase")