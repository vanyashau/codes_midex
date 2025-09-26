class Human:
    default_name = 'NoName'
    default_age = 18

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        house_info = self.__house if self.__house else 'Нет дома'
        print(f'Имя: {self.name}\Возраст: {self.age}\Деньги на счету: {self.__money}\Дом: {house_info}')

    @staticmethod
    def default_info():
        print(f'Базовое имя: {Human.default_name}, базовый возраст: {Human.default_age}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        print(f'{self.name} купил дом за {price}.')

    def earn_money(self, amount=100000):
        self.__money += amount
        print(f'{self.name} внёс на счёт {amount}. Баланс после прибавки: {self.__money}')

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
        else:
            print(f'У вас нет денег для покупки дома! Нужно {final_price}, а у вас всего лишь {self.__money}.')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

    def __repr__(self):
        return f'Дом (площадь = {self._area}, стоимость = {self._price})'


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)

    def __repr__(self):
        return f'Маленький дом (площадь = 40, цена = {self._price})'