def print_last_digit(number):
    if number > 0:
        number = number % 10
    elif number <= 0:
        number = abs(number) % 10
    print(number, end="")
    return number
