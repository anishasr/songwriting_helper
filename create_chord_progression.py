from chord_progressions import verse_progressions
from chord_progressions import chorus_progressions
from chord_progressions import chord_chart

# Making suggestions on chorus chord progression based on verse progressions
key = input("What key are we in? ") 
mode = input("Which mode are we in? ") 

# get verse progression, pass in key and mode
verse_chords = verse_progressions.build_verse(key,mode)

# get chorus progression
# # TODO - hard coded '2' to get borrowed chord from a related minor key
# mode = 2
# chorus_chords = chorus_progressions.build_chorus_borrowed(key,mode)

# write chord progression to file
chord_chart.write_section(verse_chords)
# chord_chart.write_section(chorus_chords)
