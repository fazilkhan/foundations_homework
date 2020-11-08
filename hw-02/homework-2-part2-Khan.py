# Fazil Khan
# 10/29/2020
#Homework 2, Part 2.

#LISTS.
countries = ["USA", "India", "Germany", "Singapore", "Bhutan", "New Zealand", "Argentina"]
for country in countries:
    print(country)

countries = sorted(countries)
print(countries)
print(countries[0])
print(countries[-2])

countries.remove("Germany")
print(countries)

for country in countries:
  print(country.upper())


#Dictionaries

tree = {'name': 'Candler Oak', 'species': 'Oak', 'age': 300, 'location_name': "Savannah, Georgia", 'latitude': 32.0809 , 'longitude': -81.0912}
print(tree['name'], "is a", tree['age'], "year old tree that is in", tree['location_name'])

NYC_latitude = 40.7128

if NYC_latitude > tree['latitude']:
  print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC.")
else:
  print("The tree", tree['name'], "in", tree['location_name'], "is north of NYC.")

user_age = input("How old are you?")
user_age = int(user_age)

if user_age > tree['age']:
  print("You are", user_age - tree['age'], "years older than", tree['name'])
else:
  print("You are", tree['age'] - user_age, "years younger than", tree['name'])

#LIST of DICTIONARIES.

places = [{'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
{'name': 'Tehran', 'latitude': 35.6892, 'longitude': 51.3890},
{'name': 'Falkland Islands', 'latitude': -51.7963, 'longitude': -59.5236},
{'name': 'Seoul', 'latitude': 37.5665, 'longitude': 126.9780},
{'name': 'Santiago', 'latitude': -33.4489, 'longitude': -70.6693}]

for place in places:
  if place['latitude'] > 0:
    print(place['name'], "is north of the equator.")
  elif place['latitude'] < 0 and place['latitude'] > -50:
    print(place['name'], "is south of the equator.")
  elif place['latitude'] < -50:
      print(place['name'], "is south of the equator. The Falkland Islands are a biogeographical part of the mild Antarctic zone.")


for place in places:
  if place['latitude'] > 32.0809:
    print(place['name'], "is north of the Candler oak in Savannah, Georgia.")
  elif place['latitude'] < 32.0809:
    print(place['name'], "is south of the Candler oak in Savannah, Georgia")



