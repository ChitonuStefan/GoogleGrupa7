while True:
    operator_1 = input("Adauga primul operator: ")
    operator_2 = input("Adauga al doilea operator: ")
    operatie = input("Alege operatia pe care doresti sa o executi: ")
    if (operatie in ['+', '-', '', '/'] and operator_1.isdigit() ) and operator_2.isdigit():
        if int(operator_2) ==0 and operatie == '/':
            print(f'Impartirea la 0 nu este permisa')
            continue
        if operatie  == '+':
            print(f"Suma celor 2 numere {operator_1} + {operator_2} = {int(operator_1) + int(operator_2)}")
        elif operatie  == '-':
            print(f"Diferenta celor 2 numere {operator_1} - {operator_2} = {int(operator_1) - int(operator_2)}")
        elif operatie  == '':
            print(f"Produsul celor 2 numere {operator_1} * {operator_2} = {int(operator_1) * int(operator_2)}")
        elif int(operator_2) != 0:
            print(f"Impartirea celor 2 numere {operator_1} / {operator_2} = {int(operator_1) / int(operator_2)}")
        break
    else:
        print(f"Alege o operatie din lista: {', '.join(['+', '-', '*', '/'])}")