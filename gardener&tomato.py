class Tomato:
    states = ['зеленый', 'желтый', 'оранжевый', 'красный']

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        curr_index = self.states.index(self._state)
        if curr_index < len(self.states) - 1:
            self._state = self.states[curr_index + 1]


    def ripe(self):
        return self._state == self.states[-1]


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} работает: растение зреет!")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
        else:
            print("Плоды еще не созрели, нельзя собирать урожай!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:\n- Для выращивания томатов их нужно регулярно поливать и удобрять.\n- Собирать томыты можно только, когда все томаты созрели (стали красными).")
Gardener.knowledge_base()

bush = TomatoBush(3)

gardener = Gardener("Иван", bush)

gardener.work()

gardener.harvest()

gardener.work()

gardener.harvest()

gardener.work()

gardener.harvest()

gardener.work()

gardener.harvest()