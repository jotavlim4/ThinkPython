def right_justify(s):
    space = (70-len(s))*' '
    s = space + s
    print(s)
    
right_justify("monthy")