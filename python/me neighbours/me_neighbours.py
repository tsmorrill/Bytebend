from functools import reduce
from random import choice

VERSION = '0.1c'
DESCRIPTION = 'Coming soon: scale-degrees mode!'

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
    '''Return a tuple that is equal to seq with randomized perturbations
    occuring at indices given by last variance number of values in p_indices'''
    width = len(seq)
    if variance == None:
        variance = width >> 1
    p_set = set(p_indices(width)[:width - variance - 1:-1])
    perturbation = (choice(alphabet) if i in p_set else val
                    for i, val in enumerate(seq))
    return(tuple(perturbation))
    

def welcome():
    noun = 'beat'
    action = 'nudger'
    print(f'Welcome to ME NEIGHBOURS, the Jocko Homomorphism {noun} {action}.')


def version():
    print('')
    print(f'v{VERSION}')
    print(DESCRIPTION)
    print('')


def oops():
    print('Come again?')
    print('')


def pick(options:tuple, msg=''):
    if msg != '':
        print(msg)
    verbose = (f'    {i}: {opt}' for i, opt in enumerate(options))
    for line in verbose:
        print(line)
    selection = None
    while selection is None:
        try:
            i = int(input())
            selection = options[i]
            print('')
            print(f'{i}: {selection}')
        except:
            oops()
    print('')
    return selection


def set_mode():
    options = ('rhythm', 'scale-degrees')
    return pick(options, 'Select mode:')


def help_text(mode:str):
    if mode == 'scale-degrees':
        print('Scale degrees mode?')
        print('Sure thing. Your scale has two degrees, "hit" and "rest".')
        print('See you in v0.2! :P')
        print('')

    print(f'Please enter a single, complete bar of 4/4 time.')
    print('Any power-of-two division will do: 8ths, 32nds, go nuts.')
    print('Finer divisions work better.')
    print('')



def prompt(mode:str):
    command = input("Enter your rhythm using 1's and 0's separated by spaces.\n")
    seq = tuple(int(val) for val in command.split())
    print('')
    bar = b_string(seq)
    print(f"That's {bar}.")
    print('')
    options = tuple(p_seq(seq) for _ in range(4))
    bars = tuple(b_string(opt) for opt in options)
    return bars


def b_string(bar:tuple):
    notes = ' '.join((str(val) for val in bar))
    return f'| {notes} |'


def compare(x, y):
    return pick((x, y), 'Which sounds better to you?')


def tourney_choice(options:tuple):
    return reduce(compare, options)


def report(winner):
    print(f'So go try {winner}!')


def main():
    welcome()
    version()
    mode = set_mode()
    help_text(mode)
    options = prompt(mode)
    winner = tourney_choice(options)
    report(winner)


if __name__ == '__main__':
    main()
