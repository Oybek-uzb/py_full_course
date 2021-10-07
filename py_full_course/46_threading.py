# thread => a flow of execution. Like a separate order of instructions.
# However each thread takes a turn running to achieve concurrency
# GIL (global interpreter lock) => allows only one thread to hold the control of the Python interpreter

# cpu bound => program/task spends most of it's time waiting for internal events (CPU intensive)
# use multiprocessing.

# io bound => program/task spends most of it's time waiting for external events (user input, web scraping)
# use multithreading

import threading
import time

print(threading.active_count()) # aynidamda mavjud oqimlar soni

def eat_breakfast():
    time.sleep(3)
    print("eat breakfast")

def drink_tea():
    time.sleep(4)
    print("drink_tea")

def study():
    time.sleep(5)
    print("study")

x = threading.Thread(target=eat_breakfast, args=()) # bu yerda eat_breakfast funksiya uchun yangi thread ochildi. eat_breakfast fuksiyamiz argumentlar qabul qilganida uni agrs=() dagi qavs ichida yozardik.
y = threading.Thread(target=drink_tea, args=())
z = threading.Thread(target=study, args=())

x.start() # bu yerda o'sha hosil qilingan oqim ishga tushirildi.
y.start()
z.start()

print(threading.active_count())
print(time.perf_counter()) # MainThread qancha vaqt davomida bajarilganini sekundlarda qaytaradi.

# eat_breakfast()
# drink_tea()
# study()

# yuqorida barchasi bitta thread (oqim) da bajarilgani uchun barchasi ketma-ket bo'ladi.
# Aslida esa real hayotda yuqoridagilarning barchasi bir vaqtning o'zida bajarilishi mumkin.
# Mana shu holatda endi multi-threading ni ko'ramiz.

# x.join() # x thread ni Main thread ga qo'shib yuboradi.

# daemon threading => non-daemon treading lar complete bo'lmaguncha complete bo'lmaydi
# non-daemon threading lar ma'lum vaqtdan keyin complete bo'lishi mumkin. Aytaylik timer.sleep(3) qilib qo'ysak, 3 sekunddan keyin complete bo'ladi.
# Quyidagi misoldan yanada tushunarli bo'ladi degan umiddamiz.

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        print("logged in for: {} seconds".format(count))

# x = threading.Thread(target=timer, args=())
# x.start()

# answer = input("Enter your login: ")

# Yuqorida foydalanuvchi login ini kiritgancha qancha vaqt ketishini tekshiruvchi dastur yozildi.
# Ya'ni "Enter your login" deb foydalanuvchidan login so'raladi, ayni shu damda boshqa oqimda timer ishga tushadi.
# Agar dastur shu ko'rinishda qoladigan bo'lsa, foydalanuvchi ismini kiritsa ham timer to'xtamaydi.
# Chunki biz timer ishga tushgan oqimni non-daemon qildik va unga ma'lum tugash vaqtini bermadik.
# Bizda MainThread ning ishi tugadi lekin boshqa timer-thread ishlab turibdi. Bu esa to'g'rimas.
# Aynan mana shunday holatlarning oldini olishda daemon-threading ishlatiladi.
# Tushunmovchilik bo'lmasligi uchun yuqoridagi 61, 62 va 64- satrlar comment ga olindi.

x = threading.Thread(target=timer, args=(), daemon=True) # shu tarzda timer-threading daemon-threading bo'ldi. keyword argument emas x.setDaemon(True) qilsa ham bo'ladi.
x.start()

answer = input("Enter your login: ")

# Endi esa hammasi joyida. Ya'ni foydalanuvchi login ini kiritgunicha timer-threading ishlab turadi. Kiritib bo'lishi bilan esa timer-threading ham complete bo'ladi

# x.setDaemon(True)    # yuqorida aytganimiz kabi x ni daemon yoki non-daemon qiladi. Ammo thread jarayonda bo'lib turgan paytda ishlamaydi.
# x.isDaemon()         # x-thread daemon bo'lsa True aks holda False qaytariladi.