class TriangleChecker:
    def __init__(self, first=None, second=None, third=None):
        try:
            self.sorted_numbers = sorted([int(first), int(second), int(third)])
        except Exception:
            self.sorted_numbers = None

    def is_triangle(self):
        if self.sorted_numbers is None:
            return 'Нужно вводить только числа!'
        elif any(x < 0 for x in self.sorted_numbers):
            return 'С отрицательными числами ничего не выйдет!'
        elif self.sorted_numbers[2] < self.sorted_numbers[0] + self.sorted_numbers[1]:
            return 'Ура, можно построить треугольник!'
        else:
            return 'Жаль, но из этого треугольник не сделать'

a = TriangleChecker(5, 2)
print(a.is_triangle())