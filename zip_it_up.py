import os
import zipfile

root = "U:\\tools\\mapstyles"

# old way I used to concattenate a path. 
# instead of using a hardcoded path separator you an also use os.sep 
pathsep = "\\"
resloc = root + pathsep + "results"
# but you really want to use os.path.join, pyhon adds the appropriate sep for you
# --> makes it platform independent
resloc = os.path.join(root, "results")
print(resloc)

os.chdir(root)

# without function bundle
# zfile = zipfile.ZipFile('results_v2.zip', 'w', zipfile.ZIP_DEFLATED)
# for dir_path, sub_dirs, files in os.walk("results"):
#     for file in files:
#         zfile.write(os.path.join(dir_path, file))
# zfile.close()

# with function bundle
def fillzip(path, zipfilehandle):
    # zipfilehandle is variable name that creates the zip file --> in this case: zfile below
    for dir_path, dirs, files in os.walk(path):
        for file in files:
            zipfilehandle.write(os.path.join(dir_path, file))

zfile = zipfile.ZipFile('results.zip', 'w', zipfile.ZIP_DEFLATED)
fillzip("results", zfile)
zfile.close()
