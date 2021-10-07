# exception => events detected during execution that interrupt the flow of a programm

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    # print(result)
except ZeroDivisionError as e: # 0 ga bo'lish sodir bo'lganda yuzaga keluvchi uzilish turi
    print(e) # sodir bo'lgan error haqida ma'lumot
    print("Occured division by zero!")
except ValueError as e: # son bo'lmagan qiymatga bo'lganda sodir bo'ladigan uzilish turi.
    print(e)
    print("Enter only numbers, pls!")
except Exception as e: # Exception bu ixtiyoriy tudagi uzilishlar uchun hisoblanadi. Lekin bu good practice hisoblanmaydi, chunki biz aniq qanaqa uzilish bo'lganini bilmaymiz.
    print(e)
    print("Something went wrong :(")
else:
    print(result)
    # e'tibor bergan bo'lsangiz yuqoridagi print comment qilinib bu yerga yozildi.
    # try qilinadi agar hech qanday exception sodir bo'lmasa keyin else qismga kelinadi.
finally:
    print("This will display anyway")
    # finally ni else dan farqi shundaki try ni tarkibidagi kodda exception aniqlansa ham aniqlanmasa ham finally dagi kod bajariladi.
    # else dagi kod esa faqatgina exception sodir bo'lmasa bajariladi.
