from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Gentra", "Chevrole", 2019, "Choco")

car_1.drive()
car_2.drive()
print(car_2.wheels)
print(car_1.wheels)

car_2.wheels = 2 # endi car_2 dagi balonlar soni 2 ta bo'ldi. Mototsikl ;)
print(car_2.wheels)

Car.wheels = 2 # endi esa butun boshli class ning tarkibidagi wheels ning qiymati o'zgardi.
                # endi Car ning asosida tuzilgan object larning barchasida wheels 2 ga teng bo'ladi.
