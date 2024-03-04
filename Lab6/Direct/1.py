import os

print(os.listdir())

alll = os.listdir()

for i in alll:
    if os.path.isdir(i):
        print(i, "is directory")
        
for i in alll:
    if os.path.isfile(i):
        print(i, "is file")
        
spe = r"C:\Users\Чевапчичи\Pictures"

print(os.listdir(spe))
    