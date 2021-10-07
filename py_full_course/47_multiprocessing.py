# multiprocessing => running tasks in parallel on different cpu cores, bypasses GIL used for threading
# multiprocessing => better for cpu bound tasks (heavy cpu usage)
# multithreading => better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(100,)) # args ga beriladigan qiymat tuple bo'lishi shart. Birgina (1000000000) berib qo'ysak Python xatolik beradi. Shuning uchun (1000000000,) berilsa u ikkinchi qiymat None ekan deb qaraydi.
    a.start()

    a.join()

    print(cpu_count()) # protsessorda nechta potok borligi. Yuqorida Processe bilan yangi protsess yaratildi. Bu orqali qilinadigan katta ishni kichkina qisimlarga, prosesslarga bo'lib barchasini alohida potoklarda qilish mumkin va bu ishni tezlashtiradi.
                        # bizda 8 ta potok bor ekan. Aytagnimizdek katta ishni 8 tadan ko'p kichik bo'laklarga bo'lib, ya'ni har biri uchun alohida Process qilishni foydasi yuq. Chunki ko'pi bilan 8 ta process birdaniga ishlashi mumkin.
    print("finished in: ", time.perf_counter(), " seconds")

if __name__ == "__main__":
    main()