import datetime

# get week of the year from a date

#heute = datetime.date.today()
heute = datetime.datetime.now()
print(heute)
jahr = heute.year
print(jahr)
# isocalendar retruns a named tuple with 3 components: year, week and weekday.
woy = heute.isocalendar()
# whole tuple 
print(woy)
# year
print("Year: {}".format(woy[0]))
# week of year
print("Week of Year: {}".format(woy[1]))
# day of week
print("Day of week: {}".format(woy[2]))

# I used it to string together a build ID
whatsheet = "Defect Verification"
# whatsheet = "Areas"
# whatnext = whatsheet.replace(" ", "")
# print(whatnext)
build_id = "MapStyles.{}.{}.{}".format(whatsheet.replace(" ", ""),woy[0],woy[1])

print("Build ID: {}".format(build_id))
