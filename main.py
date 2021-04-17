from random import randint


class LottoSimulator:
    # def __init__(self):
    #     # self.numbers = numbers
    #     # self.sorted_numbers = sorted_numbers
    #     # self.random_numbers = random_numbers

    def give_six_unique_numbers(self):
        i = 0
        self.numbers = []
        while i < 6:
            try:
                user_num = int(input("Please give a number from 1 - 49: "))
                if user_num in range(1, 50):
                    pass
                else:
                    print("Number should be from 1 - 49.")
                    continue
                if user_num not in self.numbers:
                    pass
                else:
                    print("Given number should not be declared before.")
                    continue
                print(f"Number {user_num} fulfills the requirements and is saved!")
                self.numbers.append(user_num)
                print(f"Your have already given following numbers:\n{self.numbers}.")
                i += 1
            except (ValueError, TypeError):
                print("Given number is invalid. Please try again.")
        return self.numbers

    def numbers_sorting(self):
        self.sorted_numbers = sorted(self.numbers)
        print(f'Your numbers are sorted: {self.sorted_numbers}.')
        return self.sorted_numbers

    def numbers_draw(self):
        i = 0
        self.random_numbers = []
        while i < 6:
            random_number = randint(1, 50)
            if random_number not in self.random_numbers:
                self.random_numbers.append(random_number)
                i += 1
            else:
                continue
        print(f'Six randomly generated numbers are {self.random_numbers}')
        return self.random_numbers

    def numbers_check(self):
        corresponding_numbers = []
        for number in self.random_numbers:
            if number in self.numbers:
                corresponding_numbers.append(number)
            else:
                continue
        print(f'You have guessed {len(corresponding_numbers)} numbers!')


play = LottoSimulator()
play.give_six_unique_numbers()
play.numbers_sorting()
play.numbers_draw()
play.numbers_check()