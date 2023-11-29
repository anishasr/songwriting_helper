import build_scale

# Find chords given scale

# TODO: refactor to determine mode based on scale
def get_diatonic_triads(scale,mode):
    chords = []
    if mode == 1:
        # in a major scale, chords built on ii, iii, vi are minor
        is_minor = {1:0, 2:1, 3:1, 4:0, 5:0, 6:1, 7:0}
    elif mode == 2:
        # in a minord scale, chords built on i and iv are minor
        is_minor = {1:1, 2:0, 3:0, 4:1, 5:0, 6:0, 7:0}

    root_pos = 0
    # start adding chords from root
    while root_pos < len(scale)-1:

        # look up each chord
        chord = scale[root_pos]
        #TODO: should I adjust the scale to match roman numerals/numbering system?
        if is_minor[root_pos+1]:
            chord += 'm'
        chords.append(chord)

        # make next note root
        root_pos += 1
    return chords

def diatonic_triad_notes(scale):
    chords = []

    # start building chords from root
    root_pos = 0
    while root_pos < len(scale)-1:
        triad_positions = [root_pos % 7, (root_pos + 2) % 7, (root_pos + 4) % 7]

        # look up each chord
        n1 = scale[triad_positions[0]]
        n2 = scale[triad_positions[1]]
        n3 = scale[triad_positions[2]]
        
        # create chord as a tuple
        chord = (n1, n2, n3)
        chords.append(chord)

        # make next note root
        root_pos += 1

    return chords

# def get_chromatic_chords():
#     intervals_major = {1:0, 2:2, 3:4, 4:5, 5:7, 6:9, 7:11}
#     intervals_minor = {1:0, 2:1, 3:3, 4:5, 5:7, 6:8, 7:10}

# FOR TESTING
def main():
    scale = build_scale.find_scale('C',1)
    c = get_diatonic_triads(scale,1)
    c1 = diatonic_triad_notes(scale)
    print(c)
    print(c1)
    # print(find_scale('D',1))
    # print(find_scale('G',1))
    # print(find_scale('F',1))

main()