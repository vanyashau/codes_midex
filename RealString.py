class RealString:
    def __init__(self, string):
        self.string = string

    def __lt__(self, other):
        if isinstance(other, RealString):
            if len(self.string) < len(other.string):
                return True
            else:
                return False
        else:
            if len(self.string) < len(other):
                return True
            else:
                return False
        
    def __le__(self, other):
        if isinstance(other, RealString):
            if len(self.string) <= len(other.string):
                return True
            else:
                return False
        else:
            if len(self.string) <= len(other):
                return True
            else:
                return False

    def __eq__(self, other):
        if isinstance(other, RealString):
            if len(self.string) == len(other.string):
                return True
            else:
                return False
        else:
            if len(self.string) == len(other):
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, RealString):
            if len(self.string) != len(other.string):
                return True
            else:
                return False
        else:
            if len(self.string) != len(other):
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, RealString):
            if len(self.string) > len(other.string):
                return True
            else:
                return False
        else:
            if len(self.string) > len(other):
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(other, RealString):
            if len(self.string) >= len(other.string):
                return True
            else:
                return False
        else:
            if len(self.string) >= len(other):
                return True
            else:
                return False

a = RealString('Яблоко')
b = 'Яблоко'
c = RealString('Apple')
d = 'Apple'

print(a == b)