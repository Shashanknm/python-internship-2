e_r="2468"
o_r="1357"

e_c="bdfh"
o_c="aceg"

s="h7"
if s[0] in e_c:
    if s[1] in e_r:
        print("black")
    else:
        print("white")
else:
    if s[1] in e_r:
        print("white")
    else:
        print("black")