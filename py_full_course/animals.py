class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal): # Animal dan nasl olinyapti
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

# yuqorida Animaldan nasl olinganligi uchun Rabbit da ham, Fish da ham, Hawk da ham Animal ning matod va field lari mavjud bo'ladi.
# shuningdek o'zlarining tarkibidagi metoda va field (yoki attribut ham deyiladi) lar ham saqlanib qoladi.
# yuqorida Animal ning tarkibida eat metodi bor. Agar bizda Rabbit ning tarkibida ham eat metodi bo'lsa Animal ning tarkibidagisi rad etiladi.