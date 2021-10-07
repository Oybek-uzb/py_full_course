animal = "dog"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item)) # yuqoridagiga alternativ
print("The {1} jumped over the {0}".format(animal, item)) # positional arguments, bu usul bilan format ni ichiga berilgan argumentlarning qaysi tartibda turgani qayerga qo'yilishi kerakligini ko'rsatish mumkin.
print("The {animal_1} jumped over the {item_1}".format(animal_1="cat", item_1="tree")) # keyword arguments
# aynan bir indeksni yoki keyword ni bir nech marta ishlatishimiz ham mumkin, print("{one} {one}".format(one="1", two="2"))

print("My name is {:10}. Nice to meet you!".format("Oybek")) # {:10} yozuvi qiymat uchun 10 ta joy ajratish degani.
print("My name is {:<10}. Nice to meet you!".format("Oybek")) # yuqoridagi bilan bir xil.
print("My name is {:>10}. Nice to meet you!".format("Oybek")) # bunda ham 10 ta joy ajratiladi yuqoridagilardan farqi ortib qolgan joy qiymatdan chap tomonga o'tkaziladi.
print("My name is {:^10}. Nice to meet you!".format("Oybek")) # bunda ham shu holat faqat ortib qolgan joy qiymatning ikki tomoniga taqsimlanadi.

# format numbers

number_pi = 3.14159
print("The number pi is {:.2f}".format(number_pi)) # number_pi dagi verguldan keyingi 2 ta sonni yaxlitlab chiqaradi.

number = 1000
print("The number is {:,}".format(number)) # 10,000 ko'rinishida yozadi, ya'ni har uch xonadan keyin (,) qo'yadi.
print("The number is {:b}".format(number)) # number ni binar ko'rinishga, ya'ni ikkilik sanoq sistemasiga o'tkazadi.
print("The number is {:o}".format(number)) # number ni sakkizlik sanoq sistemasiga o'tkazadi.
print("The number is {:x}".format(number)) # number ni o'n oltilik sanoq sistemasiga o'tkazadi. {:X} katta harflar uchun.
print("The number is {:e}".format(number)) # number ni o'nning darajasi ko'rinishida yozadi. {:E} katta harf uchun.


