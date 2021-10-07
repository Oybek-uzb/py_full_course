import random

x = random.randint(1, 7) # [1:7] oraliqdagi ixtiyoriy butun son
y = random.random() # [0, 1) oralig'idagi ixtiyoriy son

print(x)
print(y)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList) # myList ning ichidan ixtiyoriy birini tanlab beradi.

print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards) # cards ning elementlarini ixtiyoriy tartibda qo'yib beradi. Bunda cards o'zi o'zgaradi. Vawwe zarba lekin, Python respect bro. 

print(cards)