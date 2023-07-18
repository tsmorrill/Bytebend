from random import randrange

FRAMERATE = 24 # frames per second
DURATION = 96

x = randrange(1, 2 << 14)


def program(t):
    global x

    bit = x ^ x >> 1
    x >>= 1
    x += bit << 12

    return x


def main(func):
    func = mask(func)
    clock = [t for t in range(FRAMERATE)]
    data = map(func, clock)
    record(data)
    print("Have a nice day! :3")


def mask(program): # This could be a decorator
    BIT_MASK = 0b11111111111111

    def func(t):
        return program(t) & BIT_MASK
    return func


def record(data):
    for integer in data:
        print(integer)
    pass


if __name__ == "__main__":
    main(program)
