# list comprehensions => a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression (if/else) for item in iterable]

squares = []               # create an empty list
for i in range(1, 11):     # create a for loop
    squares.append(i * i)  # define what each loop iteration should do
print(squares)

squares = [i * i for i in range(1, 11)] # yuqoridagiga alternativ, faqat list comperhensiv sintaksisda yozilgan. It is so cool!
print(squares)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
passed_students = list(filter(lambda x: x >= 60, students)) # (a)
print(passed_students)

passed_students = [i for i in students if i >= 60] # yuqoridagi (a) ga alternative
print(passed_students)

passed_students = [i if i >= 60 else "FAILED" for i in students] # bu ham (a) ga qisman alternativ. Faqat bunda if dagi shartni qanoatlantirmagan qiymatlarga else dagi qiymatlar yoziladi.
print(passed_students)
