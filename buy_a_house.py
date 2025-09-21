class Human:
    default_name = 'NoName'
    default_age = 18

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}, Default age: {Human.default_age}")

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        house_info = self.__house if self.__house else "No house"
        print(f"Name: {self.name}\nAge: {self.age}\nMoney: {self.__money}\nHouse: {house_info}")

    def earn_money(self, amount=100000):
        self.__money += amount
        print(f"{self.name} earned {amount} money! Current balance: {self.__money}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        print(f"{self.name} bought a house for {price}.")

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
        else:
            print(f"Not enough money to buy the house! Need {final_price}, have {self.__money}.")

    @property
    def house(self):
        return self.__house

    @property
    def money(self):
        return self.__money

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

    def __repr__(self):
        return f"House(area={self._area}, price={self._price})"

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)

    def __repr__(self):
        return f"SmallHouse(area=40, price={self._price})"