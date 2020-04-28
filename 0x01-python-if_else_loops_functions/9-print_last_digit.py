def print_last_digit(number):
    c = number % 10
    if number > 0:
        c = number % 10
    elif number < 0:
        c = (number * -1) % 10
    elif number == 0:
        c = 0
    print(c, end="")
    return c
