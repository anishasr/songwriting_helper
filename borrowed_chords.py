import build_scale

# Output: simple chord progression incorporating one borrowed chord from the parallel minor key

key = input("What key are we in? ") 
mode = input("Which mode are we in? ") 

# get chords of parallel minor key
build_scale.find_chords(key,2)

