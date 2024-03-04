import os

print(os.access('1.py', os.R_OK))
print(os.access('1.py', os.W_OK))
print(os.access('1.py', os.X_OK))
print(os.access('1.py', os.F_OK))
print(os.access('100.py', os.F_OK))

print(os.path.exists(r"C:\Users\Чевапчичи\Pictures\Meme.png"))
print(os.path.basename(r"C:\Users\Чевапчичи\Pictures\Meme.png"))
print(os.path.dirname(r"C:\Users\Чевапчичи\Pictures\Meme.png"))


