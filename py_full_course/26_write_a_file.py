
text = "This is text for test writing to file.\nThat is awesome!"

with open("test.txt", "w") as file:
    file.write(text) # text yozilganda avvalgi text o'chib ketadi

text = "\nHave nice day!"
with open("test.txt", "a") as file: # bu yerdagi "a" modul append ni bildiradi ya'ni file dagi ma'lumotlar o'chib ketmasdan yangi yoziladigan ma'lumotlar davomidan qo'shilib ketadi.
    file.write(text)