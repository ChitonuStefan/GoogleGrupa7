class FirstClass:
    counter = 0

    def __init__(self,val=1):
        self.__first = val
        FirstClass.counter +=1

obiect_1 = FirstClass()
obiect_2 = FirstClass()
obiect_3 = FirstClass()

print(obiect_1.__dict__, obiect_1.counter)
print(obiect_2.__dict__, obiect_2.counter)
print(obiect_3.__dict__, obiect_3.counter)