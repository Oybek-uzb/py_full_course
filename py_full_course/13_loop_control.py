# break -> biz bilganimizdek loop ni sindiradi
# continue -> bilganimizdek keyingi iteratsiyaga o'tkazadi
# pass -> hech narsa qilmaslik. continue dan farq u keyingi iteratsiya o'tkazmaydi, shunchaki hech narsa qilmaydi bo'ldi

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "22-33-44-9"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 31):
    if i == 13:
        pass
    else:
        print(i)