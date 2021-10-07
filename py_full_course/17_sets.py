# set => collection which is unordered, unindexed. No duplicate values
# set is faster than list.
# set ning ichidagi ma'lumotlar ixtiyoriy tartibda turishi mumkin.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}


utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) # utensils ga dishes ni "qo'shib" yuboradi

dinner_table = utensils.union(dishes) # utensils ga dishes ni "qo'shib" yuboradi va natija sifatida yangi set ni qaytaradi. utensils o'zgarmay qoladi

for elem in dinner_table:
    print(elem)

print(utensils.difference(dishes)) # set1.difference(set2) set2 dagi bor ma'lumotlarni set1 bilan taqqoslaydi va set1 bor va set2 da yo'q ma'lumotlarni qaytaradi.
print(utensils.intersection(dishes)) # yuqaridagining teskarisi. Ya'ni ikkovida ham bor elementlarni set qilib qaytaradi.