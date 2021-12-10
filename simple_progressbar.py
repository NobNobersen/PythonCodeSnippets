# simple progress bars
locations = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

# 1st attempt: this one prints like half a christmas tree, each line is one longer than before
progress = ""
punkt = "."

for x in locations:
    if x % 10 != 0:
        progress = progress + punkt
    else:
        progress = progress + "{}".format(x)
    print(progress)

print("\n\n")
# but it would be nice to have the progress all in one line
# 2nd attempt: print function accepts end= & sep=
# end= defaults to a carriage return. if you set it empty you stay on the same line
# sep= defaults to blank. set it to empty to have no space between the individual prints
# use flush=True to print to terminal when executed
for y in locations:
    if y % 10 != 0:
        print(punkt, end="", sep="", flush=True)
    else:
        print(y, end="", sep="", flush=True)
