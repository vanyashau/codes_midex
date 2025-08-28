class KgToPounds:
    def __init__(self, __kg):
        self.kg = __kg

    def to_pounds(self):
        return self.__kg * 2.205
    
    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
        
a = KgToPounds(5)
print(a.kg)
print(a.to_pounds())
a.kg = 10
print(a.kg)
print(a.to_pounds())