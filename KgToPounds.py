class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg
        self.__pounds = kg * 2.205
    
    @property
    def pounds(self):
        return self.__pounds

    @property
    def kg(self):
        return self.__kg
    
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
            self.__pounds = new_kg * 2.205
        else:
            raise ValueError('Килограммы задаются только числами')
        
a = KgToPounds(5)
print(a.kg)
print(a.pounds)
a.kg = 10
print(a.kg)
print(a.pounds)
