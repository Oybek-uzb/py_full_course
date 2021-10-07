def hello(name):
    print("Hello, " + name)

res = hello("Oybek") # hech narsa return qilinmasa None qaytadi

print(res)

# return statement
def multiply(num1, num2):
    result = num1 * num2
    return result

res = multiply(3, 9)
print(res)

# keyword arguments
def helloByName(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

helloByName(last="Py", first="th", middle="on")

# *args => parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments.

def add(*args): 
    # arg prosta name, uga liboy boshqa nom berish mumkin
    # agar args[i] yozuvi bilan args ning biror qiymatini o'zgartirmoqchi bo'lsak xatolik yuz beradi. Chunki u tuple, tuple larni esa o'zgartirib bo'lmaydi.
    # lekin list(args) deb yozib uni list qilib olishimiz mumkin.
    sum = 0
    for i in args:
        sum += i
    return sum

result = add(1, 2, 3, 4)
print(result)

# kwargs => parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword aguments

def greeting(first, last):
    print("Hello, " + first + " " + last)

greeting(first="Oybek", last="Makhsudov")

def greetingKwargs(**kwargs):
    print("Hello, " + kwargs["first"] + " " + kwargs["middle"] + " " + kwargs["last"])

greetingKwargs(first="Oybek", last="Makhsudov", middle="Ulugbek")