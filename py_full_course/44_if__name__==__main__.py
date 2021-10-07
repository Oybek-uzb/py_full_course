# Python da __name__ ichki o'zgaruvchisi mavjud bo'lib, agar joriy module rub=n qilinsa uning qiymati "__main__" bo'ladi aks holda, o'sha module ning nomi bo'ladi.

if __name__ == "__main__":
    print("running this module directly")
else:
    print("running other module indirectly")

# joriy module run qilinsa console ga "running this module directly" chiqadi
# mana shu module boshqa module ga export qilinsa va o'sha module run qilinsa, yuqoridagi shart tekshirila va console ga "running other module indirectly" chiqadi.