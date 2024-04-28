import random

city_name = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
city_temps = {city: random.randint(20, 30) for city in city_name}
print(city_temps)
city_temps_greater = {city: temp for (city, temp) in city_temps.items() if temp > 25}

print(city_temps_greater)

print(city_temps.items())