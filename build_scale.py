# Modes - each mode has a distinct pattern of intervals, which gives it a unique sound
# dorian_mode = [0, whole, half, whole, whole, whole, half, whole]
# phrygian_mode = [0, half, whole, whole, whole, half, whole, whole]
# lydian_mode = [0, whole, whole, whole, half, whole, whole, half] 
# mixolydian_mode = [0, whole, whole, half, whole, whole, half, whole] 
# locrian_mode = [0, half, whole, whole, half, whole, whole, whole]

def get_notes():
    notes = ["C", "C#/D♭", "D", "D#/E♭", "E", "F", "F#/G♭", "G", "G#/A♭", "A", "A#/B♭", "B"]
    return notes

def get_scale_pattern(mode):
    whole = 2
    half = 1
    # major scale pattern derived from Ionian mode
    major_scale = [0, whole, whole, half, whole, whole, whole, half]
    # minor scale pattern derived from Aeolian mode
    minor_scale = [0, whole, half, whole, whole, half, whole, whole]

    if mode == 1:
        return major_scale 
    if mode == 2:
        return minor_scale 

def find_next_note(prev_note_pos,step):
    notes = get_notes()
    current_position = prev_note_pos + step
    new_note = notes[current_position % 12]
    return new_note

def find_scale(key,mode):

    # build scale based on key
    mode = int(mode)
    scale = []
    step = -1

    notes = get_notes()
    prev_note_pos = notes.index(key)
    scale_pattern = get_scale_pattern(mode)

    # add note to scale one at a time   
    for i in range(7):
        # determine whole step or half-step from previous
        step = scale_pattern[i]
        next_note = find_next_note(prev_note_pos, step)
        scale.append(next_note)
        prev_note_pos = prev_note_pos + step
    # add 8th for now
    scale.append(scale[0])
    return scale

def major_triad(key):
    return 0

# TODO - refactor to wrap around
def find_chords(key,mode):
    is_minor = {1:0, 2:1, 3:1, 4:0, 5:0, 6:1}
    chords = []
    scale = find_scale(key,mode)
    interval = 2
    root = -1
    third = -1
    fifth = -1

    # TODO: fix loop condition
    while fifth < (len(scale)-1):
        root+=1
        third = root + interval
        fifth = third + interval
        # create chord as a tuple
        chord = (scale[root], scale[third],scale[fifth])
        chords.append(chord)
    return chords

# FOR TESTING
# def main():
#     print(find_scale('C',1))
#     print(find_scale('D',1))
#     print(find_scale('G',1))
#     print(find_scale('F',1))

# main()