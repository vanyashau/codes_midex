class Tomato:
    states = ['Отсутствует', 'Цветение', 'Зелёный', 'Красный']

    def __init__(self, index):
        self._index = index
        self._state = 0

    def stage(self):
        return Tomato.states[self._state]

    def grow(self):
        if self._state == 3:
            pass
        else:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


class TomatoBush:
    def __init__(self, count):
        self.count = count
        self.tomatoes = [Tomato(i) for i in range(self.count)]

    def grow_all(self):
        for i in range(self.count):
            self.tomatoes[i].grow()

    def all_are_ripe(self):
        for i in range(self.count):
            if self.tomatoes[i].is_ripe() == False:
                return False
        return True
    
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name):
        self.name = name
        self._plant = TomatoBush(5)

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f'Урожай собран! Удалось вырастить {self._plant.count} томатов!')
            self._plant.give_away_all()
        else:
            print('Не все томаты созрели, нужно работать больше!')
    
    @staticmethod
    def knowledge_base():
        print(' Привет, у тебя в распоряжении есть целый томатный куст!\n Для того, что бы его вырастить и собрать урожай нужно соблюдать эти правила:\n ~1.На удивление, для выращивания томатов тебе нужно работать!\n Для подрастания каждого томата хватает одного присеста.\n ~2.Ты не можешь собрать урожай пока все томаты не созрели, не любим мы этого!\n ~3.Если же все томаты созрели, то флаг тебе в руки, после сбора тебе будет выдан протокол с количеством собрынных томатов!')

Gardener.knowledge_base()
a = Gardener('Вано')

while not a._plant.all_are_ripe():
    a.work()
a.harvest()