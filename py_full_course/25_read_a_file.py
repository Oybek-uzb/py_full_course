
try:
    with open("test.txt") as file:
        print(file.read()) # bu kod file ni ochadi va tarkibidagi kod bajarib bo'lingandan keyin srazi yopad.
except FileNotFoundError:
    print("That file was not found :(")
# print(file.closed) # file ni yopilganlikka tekshiradi

