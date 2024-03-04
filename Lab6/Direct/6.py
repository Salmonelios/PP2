import os
dirr = os.getcwd() + r'\Test1\for_delete'
if os.access(dirr, os.F_OK):
    os.remove(dirr)
else:
    print("file does not exist")