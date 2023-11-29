# Output: write chord progressions to file in chord chart format
num_sections = 2
num_bars = 4

def write_section(section_chords):
    f = open("chord_chart.txt", "a")
    for i in range(num_bars):
        write_bar(f,section_chords)
    f.write("\n")
    f.close()

    #open and read the file after the appending:
    f = open("chord_chart.txt", "r")

def write_bar(f,section_chords):
    for c in section_chords:
        f.write(c + " ")
    f.write("\n")
