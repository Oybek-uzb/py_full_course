# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

happy = True
print(happy)

print(happy := True) # True ni happy ga o'zlashtiradi keyin print qiladi.

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# yuqoridagi kodni walrus operatori bilan yozamiz

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food) # Tamam
