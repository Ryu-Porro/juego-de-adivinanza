import random

numero_secreto = random.randint(0, 10)
adivinanza = int(input("Escribe un número entre el 0 y el 10: "))


while numero_secreto != adivinanza:
        if adivinanza <= numero_secreto:
            print("Mayor")
            adivinanza = int(input("Intentalo de nuevo: "))
        else:
            print("menor")
            adivinanza = int(input("Intentalo de nuevo: "))

print("Lo has adivinado!")