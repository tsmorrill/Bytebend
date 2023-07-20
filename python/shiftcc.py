from random import randrange
from midiutil import MIDIFile

FILENAME = "shiftcc"
MIDI_CC = 1
MIDI_CHANNEL = 1

FRAMERATE = 24 # frames per second
DURATION = 32 # in frames

x = randrange(1, 2 << 7)


def program(t):
    global x

    carry = x ^ (x >> 1)
    carry &= 1
    x >>= 1
    x += carry << 6

    return x


def main(func):
    data = map(func, [t for t in range(DURATION)])
    midifile = process(data)

    with open(FILENAME + ".mid", "wb") as output:
        midifile.writeFile(output)

    end()


def end():
    print("Have a nice day! :3")


def process(data):
    BIT_MASK = 0b1111111
    frame_length = 1 / FRAMERATE
    midifile = init_midifile()
    frame_start = 0.0

    for n in data:
        n &= BIT_MASK
        midifile.addControllerEvent(
            track=0,
            channel=MIDI_CHANNEL,
            time=frame_start,
            controller_number=MIDI_CC,
            parameter=n
        )
        frame_start += frame_length
    return(midifile)


def init_midifile():
    file = MIDIFile(1)
    file.addTempo(track=0, time=0.0, tempo=60) # 60 BPM
    file.addTrackName(track=0, time=0.0, trackName=FILENAME)
    # MIDIUtil documentation is incorrect
    return file


if __name__ == "__main__":
    main(program)
