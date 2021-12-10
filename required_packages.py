import os

# Script to make sure required python packages are installed. if the are not, they will be installed.
# Approach 1: read list into text file & parse file
listpythonpackages = "pip list > temp.txt"
os.system(listpythonpackages)

with open('temp.txt') as f:
    installedpackages = f.read()

reqpackages = ["openpyxl", "opencv", "scikit"]
installcmd = ["pip install openpyxl", "pip install opencv-python", "python -m pip install -U scikit-image"]

for listitem, package in enumerate(reqpackages):
    if installedpackages.find(package.casefold()) != -1:
        print("Package {} is installed, All Good...".format(package))
    else:
        print("Package {} NOT found, installing now...".format(package))
        os.system(installcmd[listitem])

os.remove("temp.txt")

# Approach 2: read output straight into variable
