# dictionary => a changeable, unordered collection of unique key:value pairs.
# Fast because they use hashing, allow us to access a value quickly.

capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "Uzbekistan": "Tashkent",
    "Turkey": "Ankara"
}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Washington"})
capitals.pop("India") # ko'rsatilgan key li item ni o'chirib yuboradi
# capitals.clear() # tozalab yuboradi

print(capitals["Turkey"])
print(capitals.get("Germany")) # yuqaridagi sintaksisdan farqi mavjud bo'lmagan keyga murojaat qilinsa None qaytariladi.
print(capitals.keys())
print(capitals.values())
print(capitals.items()) # all key:value pairs

for key, value in capitals.items():
    print(key, value)