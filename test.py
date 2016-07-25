import os
path = "/home/jy/jy/learning/python/changefilder/test"
os.chdir(path)
for i in range(10):
    os.mknod("test"+str(i)+".txt")
