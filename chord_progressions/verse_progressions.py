from music_theory import build_scale as build_scale

# output options for verse chord progressions

def build_verse(key,mode):
    common_prgs = [[1,5,6,4], [6,4,1,5], [1,6,4,5], [1,4,5,4], [2,5,1,6]]
    num_beats = 4
    verse_chords = []

    # build scale and set up sections
    scale = build_scale.find_scale(key,mode)

    for i in range(num_beats):
        # TODO - how to decide which chord progression?
        interval = common_prgs[0][i] - 1 % 7
        root = scale.index(key)
        # check if chord is minor - if chord is 2, 3, or 6, concatenate an 'm'
        if interval == 1 or interval == 2 or interval == 5:
            minor = 'm'
            verse_chords.append(scale[int(root) + interval] + minor)
            # print(scale[int(root) + interval] + minor)
        else:
            verse_chords.append(scale[int(root) + interval])
            # print(scale[int(root) + interval])
    return verse_chords