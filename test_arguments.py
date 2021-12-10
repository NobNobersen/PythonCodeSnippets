#!/usr/bin/env python3
import sys

usage = "USAGE: testMapStyles.py <map style> <excel spreadsheet name> [optional build number]"
numArgs = len(sys.argv)

# making sure the right amount of arguments are passed in, not more, not less
# expecting 3 extra ones, 1st & 2nd are mandatory, 3rd is optional
if (numArgs < 3 or numArgs > 4):
    print (usage)
    sys.exit()

# 1st string is name of python file to execute
# asign value of 2nd string to style
style = sys.argv[1]
# asign value of 3rd string to whatsheet
whatsheet = sys.argv[2]

if numArgs == 4:
    overwrite_build = True
    build_number = sys.argv[3]
else:
    overwrite_build = False

print("Style passed in: {}".format(style))
print("Spreadsheet name passed in: {}".format(whatsheet))

if overwrite_build == False:
    print("Using Program generated Build ID.")
else:
    print("Overwrite Build Number with the following: {}".format(build_number))
