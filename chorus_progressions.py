import build_scale
import borrowed_chords

def build_chorus(key,mode):
    common_prgs = [[1,5,6,4], [6,4,1,5], [1,6,4,5], [1,4,5,4], [2,5,1,6]]

    # build scale and set up sections
    scale = build_scale.find_scale(key,mode)
    num_beats = 4
    chorus_chords = []

    for i in range(num_beats):
        # TODO - allow user to select chord progression
        interval = common_prgs[4][i] - 1 % 7
        root = scale.index(key)
        # check if chord is minor - if chord is 2 or 6, concatenate an 'm'
        if interval == 1 or interval == 5:
            minor = 'm'
            chorus_chords.append(scale[int(root) + interval] + minor)
            # print(scale[int(root) + interval] + minor)
        else:
            chorus_chords.append(scale[int(root) + interval])
            # print(scale[int(root) + interval])
    return chorus_chords

def build_chorus_borrowed(key,mode):
    common_prgs = [[1,5,6,4], [6,4,1,5], [1,6,4,5], [1,4,5,4], [2,5,1,6]]

    # build scale and set up sections
    scale = build_scale.find_scale(key,mode)
    num_beats = 4
    chorus_chords = []
    minor = 'm'

    for i in range(num_beats):
        # TODO - allow user to select chord progression
        interval = common_prgs[0][i] - 1 % 7
        root = scale.index(key)
        # replace chord with borrowed chord
        if int(mode) == 1:
            # check if chord is minor - if chord is 2 or 6, concatenate an 'm'
            if interval == 1 or interval == 5:
                minor = 'm'
                chorus_chords.append(scale[int(root) + interval] + minor)
                # print(scale[int(root) + interval] + minor)
            else:
                chorus_chords.append(scale[int(root) + interval])
                # print(scale[int(root) + interval])
        elif int(mode) == 2:
            # check if chord is minor - if chord is 2 or 6, concatenate an 'm'
            if i == 2:
                # get the chord to add
                borrowed_chord = borrowed_chords.get_minor_fourth()
                # replace with borrowed chord
                if borrowed_chord[1] == 1 or borrowed_chord[1] == 4 or borrowed_chord[1] == 5:
                    chorus_chords.append(borrowed_chord[0] + minor)
                else:
                    chorus_chords.append(borrowed_chord[0])
            else:
                if interval == 1 or interval == 4 or interval == 5:
                    minor = 'm'
                    chorus_chords.append(scale[int(root) + interval] + minor)
                    # print(scale[int(root) + interval] + minor)
                else:
                    chorus_chords.append(scale[int(root) + interval])
                    # print(scale[int(root) + interval])\
    return chorus_chords