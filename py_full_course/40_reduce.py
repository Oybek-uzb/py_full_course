# reduce() => apply a function to an iterable and reduce it to a single cumulative value.
# performs function on first two elements and repeats process until 1 value remains.

# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]

word = functools.reduce(lambda x, y: x + y, letters) # JS dagi reduce kabi biroz farqi bor. JS da initial qiymat berilardi. Python dagi reduce da initial qiymat argument sifatida berilgan iterable ning birinchi elementi.
print(word)

numbers = [5, 4, 3, 2, 1]

result = functools.reduce(lambda x, y: x * y, numbers)
print(result)