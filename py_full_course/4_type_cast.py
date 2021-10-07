x = 1 # int
y = 2.9 # float
z = "7" # str

y = int(y) # 2
z = float(z) # 7.0
x = str(x) # "1"

print(y)
print(z)
print(x * 4)

# shuni bilish kerakki string tipidagi float sonni int() bilan integer qilmoqchi bo'lsak error bo'ladi.
# Masalan, int('23.9') => error