class Exemplu1:

    counter = 1
    def name(self):
        return "Carmen"


class Exemplu2(Exemplu1):

    #pass
    counter = 2
    # def name(self):
    #     return "Marcela"


class Exemplu3(Exemplu2):
     pass

    # def name(self):
    #     return "Rodica"




obiect1 = Exemplu3()
# print(obiect1.name())
print(obiect1.counter)