class Soda:
    def __init__(self, addition = None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition != None:
            return f'Газировка и {self.addition}'
        else:
            return 'Обычная газировка'

a = Soda()
print(a.show_my_drink())