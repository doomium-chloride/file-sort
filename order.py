from os import listdir, renames
from os.path import isfile, join, getmtime
from math import log10, floor
from record_sort import sort
mypath = input("Target directory: ")
def D(name):
    return join(mypath,name)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
mtime = [getmtime(D(x)) for x in onlyfiles]
digits = int(floor(log10(len(onlyfiles))) + 1)
stime, index = sort(mtime)
for i in index:
    renames(D(onlyfiles[i]),D(str(i) + "-" + onlyfiles[i]))
print("Done")