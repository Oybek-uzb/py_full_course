# dictionary copmrehension => create dictionaries using an expression
# can replace for loop and certain lambda function

# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(args) for (key, value) in iterable}

cities_in_F = {"New York": 32, "Boston": 75, "Los Angels": 100, "Chicago": 50}
cities_in_C = {key: ((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

weather = {"New York": "snowing", "Boston": "sunny", "Los Angels": "sunny", "Chicago": "cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

cities = {"New York": 32, "Boston": 75, "Los Angels": 100, "Chicago": 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(desc_cities)


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"
desc_cities = {key: check_temp(value) for (key, value) in cities.items()} # check_temp ixtiyoriy miqdorda argument qabul qiluvchi funksiya bo'lishi mumkin.
print(desc_cities)