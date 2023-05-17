class Stack:

    def init(self, val_stiva=1, val_stiva2=2):
        self.stackList = []

    def push(self, val):
        self.stackList.append(val)

    def pop(self):
        self.second = 5
        value = self.stackList[-1]
        del self.stackList[-1]
        return value

    def str(self):
        return f"{self.stackList}"

obiect_1 = Stack(val_stiva2=1, val_stiva=2)
# obiect_2 = Stack()

obiect_1.third = 6
obiect_1.push(3)
obiect_1.pop()

# print(obiect_1)
# obiect_2.push(obiect_1.pop())
print(obiect_1.dict)
# print(obiect_1._StackstackList)
# print(obiect_2)

# print(obiect_1)
# print(len())
# print(len(obiect_1.stackList))
# obiect_1.push(3)
# obiect_1.push(2)
# obiect_1.push(1)
# print(obiect_1.pop())
# print(obiect_1.pop())
# print(obiect_1.pop())