#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3


import os

cwd = os.getcwd()
files = os.listdir(cwd)
path = os.path.abspath(cwd)

for myfile in files:
    print(os.path.abspath(myfile))
