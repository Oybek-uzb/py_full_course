# lambda function => function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression.
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)
# lambda parameters: expression

def double(x):
    return x * 2

double_lambda = lambda x: x * 2 # yuqoridagi funksiyaga alternativ. Qandaydir ma'noda JS dagi => funksiyalarni eslatib yuboradi.

print(double_lambda(2))

multiply = lambda x, y: x * y
print(multiply(4, 5))

add = lambda a, b, c: a + b + c
print(add(34, 45, 56))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Oybek", "Makhsudov"))

age_check = lambda age: True if age >= 18 else False
print(age_check(45))