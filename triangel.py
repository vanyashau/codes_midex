class TriangleChecker:
    def __init__(self, first=None, second=None, third=None):
        try:
            self.sorted_numbers = sorted([int(first), int(second), int(third)])
        except (ValueError, TypeError):
            self.sorted_numbers = None

    def is_triangle(self):
        if self.sorted_numbers is None:
            print('Нужно вводить только числа!')
        elif any(x <= 0 for x in self.sorted_numbers):
            print('С отрицательными числами ничего не выйдет!')
        elif self.sorted_numbers[2] < self.sorted_numbers[0] + self.sorted_numbers[1]:
            print('Ура, можно построить треугольник!')
        else:
            print('Жаль, но из этого треугольник не сделать')