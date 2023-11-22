import build_scale

notes = ["C", "C#/D♭", "D", "D#/E♭", "E", "F", "F#/G♭", "G", "G#/A♭", "A", "A#/B♭", "B"]

is_minor = {1:0, 2:1, 3:1, 4:0, 5:0, 6:1}

whole = 2
half = 1
# major scale pattern derived from Ionian mode
major_scale = [0, whole, whole, half, whole, whole, whole, half]
# minor scale pattern derived from Aeolian mode
minor_scale = [0, whole, half, whole, whole, half, whole, whole]
# Modes - each mode has a distinct pattern of intervals, which gives it a unique sound
dorian_mode = [0, whole, half, whole, whole, whole, half, whole]
phrygian_mode = [0, half, whole, whole, whole, half, whole, whole]
lydian_mode = [0, whole, whole, whole, half, whole, whole, half] 
mixolydian_mode = [0, whole, whole, half, whole, whole, half, whole] 
locrian_mode = [0, half, whole, whole, half, whole, whole, whole]

# TODO - refactor to wrap around
def find_chords(key,mode):
    scale = find_scale(key,mode)
    interval = 2
    # startingat 0 due to index of list
    note_degree = 0
    root = -1
    third = -1
    fifth = -1
    while fifth < (len(scale)-1):
        root+=1
        third = root + interval
        fifth = third + interval
        print(scale[root] + " " + scale[third] + " " + scale[fifth] + "\n")


def find_scale(key,mode):
    # build scale based on key
    scale = []
    step = -1
    # add note to major scale one at a time
    prev_note_pos = -1
    for i in range(7):
        # add root of scale
        if(i==0):
            scale.append(key)
            # find root of key
            root = notes.index(key)
            prev_note_pos=root
        else: 
            # determine whole step or half-step from previous
            if int(mode) == 1:
                # TODO: refactor into function, pass mode type as parameter
                step = major_scale[i]
                new_pos_unadjusted = prev_note_pos+step
                new_note = notes[new_pos_unadjusted % 12]
                prev_note_pos = prev_note_pos + step
                scale.append(new_note)
            elif int(mode) == 2:
                step = minor_scale[i]
                # TODO: move this code into a function
                new_pos_unadjusted = prev_note_pos+step
                new_note = notes[new_pos_unadjusted % 12]
                prev_note_pos = prev_note_pos + step
                scale.append(new_note)
            elif int(mode) == 3:
                step = dorian_mode[i]
                new_pos_unadjusted = prev_note_pos+step
                new_note = notes[new_pos_unadjusted % 12]
                prev_note_pos = prev_note_pos + step
                scale.append(new_note)
    # do this in a better way
    scale.append(key)
    print("KEY OF " + key + " SCALE: ")
    print(scale)
    print()
    return scale


