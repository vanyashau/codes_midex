class Nikola:
    __slots__ = ('name', '__age')

    def __init__(self ,name, age):
        if name == 'Николай':
            self.name = name
        else:
            self.name = f'Я не {name}, а Николай'
        if isinstance(age, int) and age > 0:
            self.age = age
        else:
            raise ValueError('Возраст может быть только целым положительным числом')
        
    def __str__(self):
        return f'{self.name}; {self.__age} лет'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Возраст может быть только целым положительным числом')

a = Nikola('Никола', 10)
print(a)