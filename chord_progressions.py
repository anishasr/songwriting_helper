import build_scale

# A program to find chord progressions for given key

common_prgs = [[1,5,6,4], [6,4,1,5], [1,6,4,5], [1,4,5,4], [2,5,1,6]]

key = input("What key are we in? ") 
mode = input("Which mode are we in? ") 

scale = build_scale.find_scale(key,mode)

for i in range(4):
    interval = common_prgs[0][i] - 1 % 7
    root = scale.index(key)
    # check if chord is minor - if chord is 2 or 6, concatenate an 'm'
    if interval == 1 or interval == 5:
        minor = 'm'
        print(scale[int(root) + interval] + minor)
    else:
        print(scale[int(root) + interval])


