def collatz(value):
    if value % 2 == 0:
        new_value = value//2
    elif value != 1:
        new_value = 3*value+1
    else:
        new_value = 1
    print(value)
    return new_value


def recursive_collatz(value):
    while value > 1:
        value = collatz(value)
    print(1)


if __name__ == "__main__":
    """[summary]"""
    recursive_collatz(3)
