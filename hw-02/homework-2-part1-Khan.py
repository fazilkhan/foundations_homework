# Fazil Khan
# 10/29/2020
# Homework 2, Part 1.

#LISTS.
# Create list of numbers and display elements in the list.
num = [22, 90, 0, -10, 3, 22, 48]
print(len(num))
print(num[3])
print(num[1] + num[3])

num_sorted = sorted(num)
print(num_sorted[-2])

print(num[-1])
print(sum(num) / 2)

import statistics

if statistics.mean(num) > statistics.median(num):
    print("Mean is higher than median.")
else:
    print("Median is higher than mean.")


#DICTIONARIES

#Create disctionary movie.
movie = {'title': 'Anand', 'year': '1971', 'director': 'Hrishikesh Mukherjee'}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie['budget'] = 5
movie['revenue'] = 17

profit_loss = movie['revenue'] - movie['budget']
print(profit_loss)

if profit_loss < movie['budget']:
  print("That was a bad investment.")
elif profit_loss >= movie['budget'] * 5:
  print("That was a great investment.")
else:
  print("That was an okay investment.")

#Create dictionary population. All figures in millions.
population = {'Manhattan': 1.6, 'Brooklyn': 2.6, 'Bronx': 1.4, 'Queens': 2.3, 'Staten Island': 0.47}

print("Brooklyn's population is", population['Brooklyn'], "million.")

total_NYC_population = sum(population.values())

print("The total population of NYC is", total_NYC_population )
print(round(population['Manhattan'] / total_NYC_population * 100), "percent of the total NYC population lives in Manhattan.")

#ENDS