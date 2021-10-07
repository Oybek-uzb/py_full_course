import os
import shutil

path = "copy.txt"
pathDir = "for_test"
os.remove(path) # bu metod file o'chirish uchun
os.rmdir(pathDir) # bunisi esa folder o'chirish uchun. Ammo bu ham tarkibida boshqa fayl yoki papkalar bor folder ni o'chirolmaydi.
shutil.rmtree(pathDir) # mana bu esa tarkibida fayllari bo'lgan folder ni ham ishidagi barcha fayllari bilan birga "yo'q" qilib yuboradi :).
