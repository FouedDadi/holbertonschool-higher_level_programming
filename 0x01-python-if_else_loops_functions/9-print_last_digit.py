def print_last_digit(number):
    c = number % 10
    if number > 0:
        c = number % 10
    elif number < 0:
        c = (abs(number) % 10)
    print("{}".format(c), end="")
    return c
