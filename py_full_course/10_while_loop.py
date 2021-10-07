# while => bizga tanish while Python da ham sharti False bo'lib qolgancha ishlaydi.

isEntered = False
name = None

print(True + 1) # 2

while not(isEntered):
    name = input("Enter your name: ")

    if name.isalpha():
        isEntered = True

print("Hello, " + name)
