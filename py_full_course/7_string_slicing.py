# slicing => string dan ma'lum qismlarni olib boshqa string yasash
# bu indexing[] yoki slice() bilan amalga oshiriladi
# [start:stop:step]

name = "Farxod Rajabov"

first_name = name[0] # shunchaki name ning 0-elementi
first_name = name[0:6] # [0:6) oraliq
first_name = name[:6] # yuqoridagi bilan bir xil
last_name = name[7:14]
last_name = name[7:] # yuqoridagi bilan bir xil
last_name = name[7:14:2] # [7:14) oraliqdagi faqat juft larni oladi. 7- indeks 0 deb qaraladi, 8- indeks 1 deb va ...
last_name = name[7::2] # yuqoridagiga alternativ 
sliced = name[::2] # tushunarli
reversed_name = name[::-1] # stringni teskari tartibga keltiradi


print(reversed_name)

text = "Golang"

slice = slice(2, len(text)+1)

print(slice)
print(text[slice])


