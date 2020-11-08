# Fazil Khan
# 10/27/2020
# Homework-1

# Ask about user's age.
birth_year = input("Tell me what year you were born in and I'll tell you some cool facts about your life on Earth.")
birth_year = int(birth_year)

# All number based calculations.
age = 2020 - birth_year
lifetime_heartbeats = age * 365 * 24 * 60 * 72
lifetime_heartbeats_bluewhale = age * 365 * 24 * 60 * 6
lifetime_heartbeats_rabbit = age * 365 * 24 * 60 * 205
age_on_venus = (age * 365) / 225
age_on_neptune = (age * 365) / (164 * 365)
odd_even_year = birth_year % 2
president_in_office = 2020 - age
younger_older = 23 - age
older_younger = age - 23

# List of if statements.
if odd_even_year == 1:
    print("You were born in an odd year.")
else:
    print("You were born in an even year.")
if birth_year >= 2017 and birth_year <=2020:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", younger_older, "year(s) younger than the guy who wrote this program.")
    print("There has been no Democratic President since you were born.")
    print("Donald Trump was in office when you were born.")
elif birth_year >= 2009 and birth_year <= 2016:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", younger_older, "year(s) younger than the guy who wrote this program.")
    print("There has been one Democratic President since you were born.")
    print("Barack Obama was in office when you were born.")
elif birth_year >= 2001 and birth_year <= 2008:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", younger_older, "year(s) younger than the guy who wrote this program.")
    print("There has been one Democratic President since you were born.")
    print("George W. Bush was in office when you were born.")
elif birth_year >= 1997 and birth_year <= 2000:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", younger_older, "year(s) younger than the guy who wrote this program.")
    print("There have been two Democratic Presidents since you were born.")
    print("Bill Clinton was in office when you were born.")
elif birth_year == 1996:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are as old as the guy who wrote this program.")
    print("There have been two Democratic Presidents since you were born.")
    print("Bill Clinton was in office when you were born.")
elif birth_year >= 1993 and birth_year <= 1995:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been two Democratic Presidents since you were born.")
    print("Bill Clinton was in office when you were born.")
elif birth_year >= 1989 and birth_year <= 1992:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been two Democratic Presidents since you were born.")
    print("George H.W. Bush was in office when you were born.")
elif birth_year >= 1981 and birth_year <= 1988:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been two Democratic Presidents since you were born.")
    print("Ronald Reagan was in office when you were born.")
elif birth_year >= 1977 and birth_year <= 1980:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been three Democratic Presidents since you were born.")
    print("Jimmy Carter was in office when you were born.")
elif birth_year >= 1974 and birth_year <= 1977:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been three Democratic Presidents since you were born.")
    print("Gerald Ford was in office when you were born.")
elif birth_year >= 1969 and birth_year <= 1973:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been three Democratic Presidents since you were born.")
    print("Richard Nixon was in office when you were born.")
elif birth_year >= 1964 and birth_year <= 1968:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been four Democratic Presidents since you were born.")
    print("Lyndon B. Johnson was in office when you were born.")
elif birth_year >= 1961 and birth_year <= 1963:
    print("Your age is", age, "years.")
    print("Your heart has beaten approximately", (round(lifetime_heartbeats / 1000000)), "million times since you were born.")
    print("A blue whale's heart has beaten", (round(lifetime_heartbeats_bluewhale / 1000000)), "million times since you were born.")
    print("A rabbit's heart has beaten", (round(lifetime_heartbeats_rabbit / 1000000)), "million times since you were born.")
    print("Your age would be", (round(age_on_venus, 2)), "years on Venus.")
    print("Your age would be", (round(age_on_neptune, 2)), "years on Neptune.")
    print("You are", older_younger, "year(s) older than the guy who wrote this program.")
    print("There have been five Democratic Presidents since you were born.")
    print("John F. Kennedy was in office when you were born.")
else:
    print("Seriously? Go back and put in a valid year this time.")
#End of Code.
