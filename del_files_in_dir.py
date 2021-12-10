import os

resloc = "U:\\tools\\mapstyles\\results"

os.chdir(resloc)

# delete all files in directory --> loop over each file in directory and delete it 
for i in os.listdir(resloc):
    os.remove(i)
