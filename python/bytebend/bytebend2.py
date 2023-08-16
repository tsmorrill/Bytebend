from random import randrange
from pprint import pprint
from midiutil import MIDIFile

C4 = 60
D4 = 62
E4 = 64
F4 = 65
G4 = 67
A4 = 69
B4 = 71
C5 = 72
D5 = 74
E5 = 76
F5 = 77
G5 = 79
A5 = 81
B5 = 83
C6 = 84

PHRYGIAN = (D4, E4, F4, G4, A4, B4, C5, D5, E5, F5, G5, A5, B5)
GAMUT = PHRYGIAN

MAX_NOTES = 32 # 128

FILENAME = "bytebend-lfsr"
MIDI_CHANNEL = 0

FRAME_TICKS = 40 # 960 ticks = 1 quarter note


def dirty_lfsr(init:int=0b1001):
    count = 0
    register = init
    while True:
        yield register + ((count >> 2) % 4)
        count = (count + 1) & 0b10000
        x = register ^ (register >> 1)
        x ^= count >> 4
        x &= 1
        register >>= 1
        register += (x << 4)


def pitch(index:int):
    match index:
        case None:
            output = None
        case int:
            index &= 0b111
            output = GAMUT[index]
    return output


def main():
    rhythm1 = (1, 0, 1, 1, 0, 1, 1, 0)
    rhythm2 = (1, 1, 1, 1, 0, 1, 0, 1)
    phrase = 3*rhythm1 + rhythm2
    song = 16 * phrase
    trigs = (bool(n) for n in song)
    rng = dirty_lfsr()
    random = (next(rng) if trig else None for trig in trigs)
    notes = tuple(map(pitch, random))
    print(notes)

if __name__ == "__main__":
    main()
