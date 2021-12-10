import os

# print all files of a directory to the terminal
resloc = "U:\\git\\PythonCodeSnippets"

os.chdir(resloc)

# delete all files in directory --> loop over each file in directory and delete it 
for i in os.listdir(resloc):
    print(i)
