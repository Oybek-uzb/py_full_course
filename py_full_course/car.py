class Car:

    wheels = 4 # class variable
    # wheels ni __init__ (ya'ni konstruktor) ni ichida argument sifatida berishdan ma'no yo'q. Chunki barcha mashinalar uchun balonlar soni shartli ravishda 4 ta.
    # Shuning uchun wheels class ning ichida default qilib o'rnatib qo'yildi.
    def __init__(self, make, model, year, colour):
        self.make = make # instance variable
        self.model = model # instance variable
        self.year = year # instance variable
        self.colour = colour # instance variable

    def drive(self):
        print("This {} car is driving!".format(self.make))

    def stop(self):
        print("This car is stop!")