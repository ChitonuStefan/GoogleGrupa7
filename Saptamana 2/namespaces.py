from functii2 import functie_2

variabila1 = 2
a = 3
b = 2
msg = 3


def functie_1(a,b):
    # global msg
    # msg = 'Hello'
    variabila1 = a + b
    return variabila1


print(msg, 'rand16')
suma = functie_1(1, 2)
print(msg, 'rand14')
print(suma)

functie_2(4,5)