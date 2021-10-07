# sort() method => used with lists
# sort() function => used with iterables

students = ["Asadbek", "Shohruh", "Islom", "Shahlo", "Shohjahon", "Aziza", "Ilhom"]

students.sort() # students ni o'zini o'zgartiradi. Alifbo bo'yicha tartiblaydi.
# students.sort(reverse=True) # bu kod esa studentni alifboga teskari tartibda saralaydi.

for i in students:
    print(i)

students = ("Asadbek", "Shohruh", "Islom", "Shahlo", "Shohjahon", "Aziza", "Ilhom") # bu tuple bo'lganligi sababli endi u uchun sort metodi yo'q. sort() metod faqat list lar uchun mavjud.
# Lekin tuple uchun sort funksiyasi bor.

sorted_students = sorted(students) # bunda ham sorted(students, reverse=True) qilinsa teskari tartibda bo'ladi.

for i in sorted_students:
    print(i)


students = [ 
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr.Krabs", "C", 78)
] # ko'rib turganimizdek students tuple lardan iborat list

students.sort() # bunda tuple lardagi birinchi column lar, ya'ni "Squidward", "Sandy", "Patrick" va h.k lar bo'yicha alifbo tartibida saralanadi.

grade = lambda grades: grades[1]
students.sort(key=grade) # bu yerdagi grade funksiya. "key=" keyword argumenti bilan qaysi column asosida saralash ko'rsatiladi
# bu yerda grade ga argument sifatida students ning katma-ket barcha elemntlari beriladi.
# students.sort(key=grade, reverse=True) # tushunarli