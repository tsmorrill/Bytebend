from functools import reduce
from random import choice

VERSION = '0.1a'

# my neighbors are always listening to really loud drum and bass
# whether they like it or not!
#                                    @happyharryarbuckle, TikTok

def reverse(n:int, log_width:int):
    temp = '{:0{w}b}'.format(n, w=log_width)
    return int(temp[::-1], 2)


def p_indices(width:int):
    bit_width = width.bit_length() - 1
    p_order = (reverse(i, bit_width) for i in range(width))
    return tuple(p_order)


def p_seq(seq:tuple, *, variance:int=None, alphabet:tuple=[0, 1]):
    """Return a tuple that is equal to seq with randomized perturbations
    occuring at indices given by last variance number of values in p_indices"""
    width = len(seq)
    if variance == None:
        variance = width >> 1
    p_set = set(p_indices(width)[:width - variance - 1:-1])
    print(p_set)
    perturbation = (choice(alphabet) if i in p_set else val
                    for i, val in enumerate(seq))
    return(tuple(perturbation))
    

def compare(x, y):
    print("")
    print("Which do you prefer?")
    print(f"1: {x}")
    print(f"2: {y}")
    print("")
    output = None
    while output is None:
        match input("Type 1 or 2: "):
            case '1':
                output = x
            case '2':
                output = y
    return output

def tourney_choice(options:tuple):
    return reduce(compare, options)


def main():
    print("Welcome to ME NEIGHBOURS, the Jocko Homomorphism beat nudger.")
    print("")
    print(f"v{VERSION} - Please enter  acomplete, single bar of 4/4 time.")
    print("Any power-of-two division will do: quarters, 32nds, go nuts.")
    print("")
    command = input("Enter your rhythm using 1's and 0's separated by spaces.\n")
    seq = tuple(int(val) for val in command.split())
    options = tuple(p_seq(seq) for _ in range(4))
    winner = tourney_choice(options)
    print("")
    print(f"Maybe {winner} will sound nice.")


if __name__ == "__main__":
    main()
