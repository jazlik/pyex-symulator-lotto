from random import randint

def give_six_unique_numbers():
    i = 0
    numbers = []
    while i < 6:
        try:
            user_num = int(input("Please give a number from 1 - 49: "))
            if user_num in range(1, 50):
                pass
            else:
                print("Number should be from 1 - 49.")
                continue
            if user_num not in numbers:
                pass
            else:
                print("Given number should not be declared before.")
                continue
            print(f"Number {user_num} fulfills the requirements and is saved!")
            numbers.append(user_num)
            print(f"Your have already given following numbers:\n{numbers}.")
            i += 1
        except (ValueError, TypeError):
            print("Given number is invalid. Please try again.")
    return numbers


def numbers_sorting(list_of_numbers):
    sorted_numbers = sorted(list_of_numbers)
    print(f'Your numbers are sorted: {sorted_numbers}.')
    return sorted_numbers


def numbers_draw():
    i = 0
    random_numbers = []
    while i < 6:
        random_number = randint(1, 50)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
            i += 1
        else:
            continue
    print(f'Six randomly generated numbers are {random_numbers}')
    return random_numbers


numbers_sorting(give_six_unique_numbers())
numbers_draw()


