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

def dirty_lfsr(init:int=0b001):
    count = 0
    register = init
    while True:
        yield register + ((count >> 6) & 3)
        count = count + 1
        x = register ^ (register >> 2)
        # x ^= count >> 2
        x &= 1
        register >>= 1
        register += (x << 2)


def pitch(index:int):
    match index:
        case None:
            output = None
        case int:
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
    file = MIDIFile()
    file.addTrackName(track=0, time=0.0, trackName="dirty lfsr")
    for pos, note in enumerate(notes):
        if type(note) == int:
            file.addNote(track=0,
                         channel=0,
                         pitch=note,
                         time=pos*(1/2),
                         duration=1/2,
                         volume=127)
    with open("dirty_lfsr.mid", "wb") as output:
        file.writeFile(output)
        print(f"Created file 'dirty_lfsr.mid'.")

if __name__ == "__main__":
    main()
