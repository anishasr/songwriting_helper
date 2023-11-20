import build_scale

# A program to find chord progressions for given key

notes = ["C", "C#/D♭", "D", "D#/E♭", "E", "F", "F#/G♭", "G", "G#/A♭", "A", "A#/B♭", "B"]

is_minor = {1:0, 2:1, 3:1, 4:0, 5:0, 6:1}
common_prgs = [[1,5,6,4], [6,4,1,5], [1,6,4,5], [1,4,5,4], [2,5,1,6]]

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

key = input("What key are we in? ") 
mode = input("Which mode are we in? ") 

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

for i in range(4):
    interval = common_prgs[0][i] - 1 % 7
    root = scale.index(key)
    # check if chord is minor - if chord is 2 or 6, concatenate an 'm'
    if interval == 1 or interval == 5:
        minor = 'm'
        print(scale[int(root) + interval] + minor)
    else:
        print(scale[int(root) + interval])


