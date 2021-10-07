# zip(*iterables) => aggregate elements from two or more iterables (lists, tuples, sets)
# creates a zip object with paired elements stored in tuple for each element

user_names = ["Oybek", "Shohjahon", "Farxod"]
passwords = ("120501", "1979_2001_2007_2012", "080000")

users = zip(user_names, passwords) # bu yerda user_names va passwords dagi mos elementlar juft-juft qilib tuple lar yasalyapti.
# zip qaytaradigan natija zip object bo'ladi. Lekin uni list(), tuple(), set() yordamida cast qilish mumkin
# users = set(users)
users = dict(users)
# zip object hatto dictionary qilish ham mumkin. Bunda birinchi argument sifatida berilgan iterable ning elementlari key, ikkinchisiniki esa value bo'ladi.

for key, value in users.items():
    print(key + ": " + value)

login_dates = ["12/05/2001", "31/07/2007", "01/01/2000"]

users = zip(user_names, passwords, login_dates) # bu yerda esa 3 ta iterable dan mos elementlar olinib, har biri tuple qilinadi.

for i in users:
    print(i)