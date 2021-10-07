import os

source = "test.txt"
destination = "/home/oybek/Desktop/new.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source, destination)
        print(source + " was moved.")
except FileNotFoundError as e:
    print(e)
