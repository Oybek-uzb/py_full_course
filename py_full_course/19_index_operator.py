# index operator [] = gives access to a sequence's element (str, list, tuple)

name = "Farkhod Radjabov"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[:7].upper()
last_name = name[8:].lower()
last_character = name[-1]

print(last_character)