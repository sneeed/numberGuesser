import random as rnd
import time as tm

waiting_time = 0  # preset is 2 # for Testing
# waiting_time = 2  # preset is 2


def welcome():
    print("Hello, let's play a little game.")
    tm.sleep(waiting_time / 2)
    print("I think of a secret number and you then guess it.")
    tm.sleep(waiting_time)


def define_number_area():
    print("Please set in which number area my secret number should be.")
    tm.sleep(waiting_time)
    smallest_number = read_smallest_number()
    biggest_number = read_biggest_number()
    print("So my secret number should lay between " + str(smallest_number) + " and " + str(biggest_number) + " (inclusively).")
    return smallest_number, biggest_number


def read_smallest_number():
    while True:
        try:
            number = int(input("What would be the smallest value of the number area my secret number should be in?\n"))
            break
        except ValueError:
            print("You didn't enter a valid number. Please try again.")
            continue
    return number


def read_biggest_number():
    while True:
        try:
            number = int(input("What would be the biggest value of the number area my secret number should be in?\n"))
            break
        except ValueError:
            print("You didn't enter a valid number. Please try again.")
            continue
    return number


def check_if_valid_number(input_number):
    return input_number.isdecimal()


def calculate_secret_number(smallest_number, biggest_number):
    return rnd.randint(smallest_number, biggest_number)


def ask_for_secret_number(secret_number, biggest_number, smallest_number):
    if biggest_number - smallest_number == 0:
        print("Nah, that's too easy. With such a small number range the secret number must be " + str(biggest_number) + ".")
        return
    input_number = None

    while not is_number_guess_correct(input_number, secret_number):
        if input_number:  # checks if input_number is None and thus has't been entered yet
            print("No, " + str(input_number) + " is not my secret number.")
            print("----------------------------------")
            biggest_number, smallest_number = give_hint(secret_number, biggest_number, smallest_number)
        input_number = int(input("What do you think is my secret number?\n"))
        tm.sleep(waiting_time / 2)

    print("\\(＾O＾)／\nCongratulations, you guessed my secret number. It was " + str(input_number) + ".")


def give_hint(secret_number, biggest_number, smallest_number):
    no_of_hint_types = 3
    if secret_number == smallest_number:
        switcher = rnd.randint(2, no_of_hint_types)
    elif secret_number == biggest_number:
        switcher = rnd.randint(1, 2)
    elif secret_number > 1:
        switcher = rnd.randint(1, no_of_hint_types)
    # switcher = 3  # for testing

    if switcher == 1:
        smallest_number = give_hint_bigger(secret_number, smallest_number)

    elif switcher == 2:
        biggest_number = give_hint_smaller(secret_number, biggest_number)

    elif switcher == 3:
        give_hint_multiple(secret_number)

    return biggest_number, smallest_number


def give_hint_bigger(secret_number, smallest_number):
    some_number_smaller_than_secret_number = (rnd.randint(smallest_number, secret_number - 1))
    print("My secret number is bigger than " + str(some_number_smaller_than_secret_number) + ".")
    return some_number_smaller_than_secret_number


def give_hint_smaller(secret_number, biggest_number):
    some_number_bigger_than_secret_number = (rnd.randint(secret_number + 1, biggest_number))
    print("My secret number is smaller than " + str(some_number_bigger_than_secret_number) + ".")
    return some_number_bigger_than_secret_number


def give_hint_multiple(secret_number):
    # Calculate some possible multiples of my secret number
    multiple_of = [False, True]  # no number is multiple of 0, all numbers are multiple of 1
    for num in range(2, secret_number):
        if secret_number % num == 0:
            multiple_of.append(True)
        else:
            multiple_of.append(False)

    # Select randomly a multiple and print its value
    # print("for testing: " + str(multiple_of))
    maximum = min(secret_number, 20)
    multiple_of_number = rnd.randint(2, maximum)
    is_multiple = multiple_of[multiple_of_number]
    is_multiple_string = "a" if is_multiple else "no"
    print("My secret number is " + is_multiple_string + " multiple of " + str(multiple_of_number) + ".")


def is_number_guess_correct(guessed_number, secret_number):
    return guessed_number == secret_number


if __name__ == '__main__':
    welcome()

    smallest_number, biggest_number = define_number_area()
    # smallest_number, biggest_number = 0, 10  # for testing

    tm.sleep(waiting_time)
    secret_number = calculate_secret_number(smallest_number, biggest_number)
    print("For testing: secret_number ist " + str(secret_number))  # for testing

    ask_for_secret_number(secret_number, biggest_number, smallest_number)
