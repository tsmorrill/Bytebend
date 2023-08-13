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
DURATION = 96 * 16 # in frames

ARRAY_LENGTH = 4
lfsr = 1
taps = 0b0011

def advance(time):
    global taps
    global lfsr
    taps ^= (time >> 1) % 16
    x = lfsr ^ taps
    x = x ^ (x >> 1) ^ (x >> 2)
    x &= 1
    lfsr >>= 1
    lfsr += x << (ARRAY_LENGTH - 1)


def pitch(time):
    global lfsr
    offset = (time >> 4) % 4
    index = (lfsr + offset) % len(GAMUT)
    pitch = GAMUT[index]
    advance(time)

    return pitch


def main():
    print(f"LFSR initialized to {lfsr:>04b}")
    print(list(map(pitch, range(MAX_NOTES))))


if __name__ == "__main__":
    main()
