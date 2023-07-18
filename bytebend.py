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


def main():
    DATA_MASK = 0b11111111111111
    for t in range(FRAMERATE):
        data = program(t) & DATA_MASK
        record(data)
    print("Have a nice day! :3")


def record(data):
    print(data)
    pass


if __name__ == "__main__":
    main()
