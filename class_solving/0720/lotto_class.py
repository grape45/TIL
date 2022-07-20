import random

class Lotto:
    def generate_lotto(self):
        self.numbers = sorted(random.sample(range(1, 46), 6))

    def get_money(self, real_numbers):
        print('당신의 숫자는', self.numbers)
        print('당첨 숫자는', real_numbers)
        if self.numbers == real_numbers:
            return 10,000,000,000
        else:
            return 0

lotto = Lotto()
lotto.generate_lotto()
print(lotto.numbers)
print(lotto.get_money([1, 2, 3, 4, 5, 6]))