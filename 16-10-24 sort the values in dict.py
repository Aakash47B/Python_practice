"""Filter the values in ascending order"""

city_country = {'Chennai': 'India',
                'Agra': 'India',
                'Vancour': 'Canada',
                'Tokyo': 'Japan',
                'New York': 'USA',
                'Los Angeles': 'USA',
                'San Diego': 'USA',
                'San Francisco': 'USA',
                'Madurai': 'India'}

# city_names = sorted(list(city_country.keys()))
# for city in city_names:
#    country = city_country.get(city)
#    print(f'{city} - {country}')

# ========================================================================
# country_names = []
# for place in city_country.values():
#    if place not in country_names:
#       country_names.append(place)

# country_names = sorted(set(city_country.values()))

country_names = list(dict.fromkeys(city_country.values()))

for country in country_names:
   for city in city_country:
      if country == city_country[city]:
         print(f'{country} - {city}')

