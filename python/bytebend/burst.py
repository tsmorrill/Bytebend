from functools import reduce
from midiutil import MIDIFile

MIDI_NOTE = 60
SUBDIVISION = 1/16

HITS = 9
BURSTS = 5
LENGTH = 16 

def remainders(dividend:int, divisor:int):
    residue = dividend % divisor
    return (tuple(1 for _ in range(residue))
            + tuple(0 for _ in range(divisor - residue)))


def partition(dividend:int, r_seq:iter):
    return tuple(dividend//len(r_seq) + r for r in r_seq)


def run_length(hits:int, bursts:int, length:int):
    rests = length - hits
    return zip(partition(hits, remainders(hits, bursts)[::-1]),
               partition(rests, remainders(rests, bursts)))


def burst_single(pair:tuple):
    x, y = pair
    return tuple(True for _ in range(x)) + tuple(False for _ in range(y))


def burst_mult(run_seq:iter):
    return reduce(lambda x, y: x + burst_single(y), run_seq, ())


def midi_file(track_name:str):
    file = MIDIFile(
        numTracks=1,
        ticks_per_quarternote=960,
        eventtime_is_ticks=False
    )
    file.addTrackName(track=0, time=0.0, trackName=track_name)
    # MIDIUtil documentation is incorrect
    return file


def render(trig_seq:iter, name:str):
    file = midi_file(track_name=name)
    for pos, trig in enumerate(trig_seq):
        if trig:
            file.addNote(track=0,
                         channel=0,
                         pitch=MIDI_NOTE,
                         time=pos*SUBDIVISION,
                         duration=SUBDIVISION,
                         volume=127)            
    with open(name + ".mid", "wb") as output:
        file.writeFile(output)    
        print(f"Created file '{name}.mid'.")


def main():
    render(trig_seq=burst_mult(run_length(HITS, BURSTS, LENGTH)),
           name=f"burst {HITS}, {BURSTS}, {LENGTH}")
   

if __name__ == "__main__":
    main()
