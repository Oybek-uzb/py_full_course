# while loop biror shart asosida cheksiz takrorlashi mumkin;
# for loop esa faqatgina ma'lum chegarada takrorlaydi
import time

for i in range(10):
    print(i+1)

for i in range(10, 100):   # [10, 100) oraliq
    print(i)

for i in range(1, 9, 2):   # [1, 9) oraliq, qadam 2 => 1, 3, 5, 7
    print(i)

for i in "Oybek":    # har bir belgi i ga o'zlashtiriladi
    print(i)

for second in range(10, 0, -1):
    print(second)
    time.sleep(0.1)
