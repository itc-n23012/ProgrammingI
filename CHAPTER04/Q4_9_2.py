import os
import sys

MAX = 2
print(sys.getdefaultencoding())
print(os.path.basename(os.getcwd()))

for i in range(3):
    print(i, end=" ")
    print(MAX) if MAX > i else print("#")
