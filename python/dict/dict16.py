from random import randrange
from midiutil import MIDIFile

FILENAME = "dict"
MIDI_CHANNEL = 0

FRAME_TICKS = 40 # 960 ticks = 1 quarter note
DURATION = 96 * 16 # in frames

C3 = 60
D3 = 62
E3 = 64
F3 = 65
G3 = 67
A3 = 69
B3 = 71
C4 = 72
REST = None


def duration(duration):
    return lambda pitch: (duration, pitch)


quarter = duration(4)
eigth = duration(2)
sixteenth = duration(1)


def some(func):

scale = [
    eigth(C3),
    eigth(D3),
    eigth(E3),
    eigth(F3),
    eigth(G3),
    eigth(A3),
    eigth(B3),
    eigth(C4),
    ]




if __name__ == "__main__":
    print(scale)
