cuvant = 'onomatopee'.lower()
cuvantinitial = list(cuvant)

"""o  o   _ o_e e"""
"""literele sunt lowercase"""
"""avem 7 incercari"""
"""ii dam posibilitatea utilizatorului sa nu scada din vieti daca incearca de 2 ori aceeasi litera"""

# litera_incercata = input("Alege o litera: ")
# print(litera_incercata)

for index, value in enumerate(cuvant_initial):
    # print(index, value)
    if cuvant_initial[0] != value and cuvant_initial[-1] != value:
        cuvantinitial[index] = ''
print(" ".join(cuvant_initial))

numar_incercari = 1
set_litere_incercate = set()

while numar_incercari <= 2:
    litera_incercata = input("Alege o litera: ").lower()
    if litera_incercata in cuvant_initial:
        print("Litera deja este afisata pe ecran")
    elif litera_incercata in cuvant:
        for index, value in enumerate(cuvant):
            if litera_incercata == value:
                cuvant_initial[index] = litera_incercata
    else:
        if litera_incercata in set_litere_incercate:
            print(f"Ai incercat deja aceasta litera. Literele incercate sunt: {','.join(set_litere_incercate)}")
        else:
            set_litere_incercate.add(litera_incercata)
            numar_incercari += 1
            if numar_incercari == 3:
                print(f"Ai pierdut! Cuvantul initial era: {cuvant}")
                break

    print(cuvant_initial)