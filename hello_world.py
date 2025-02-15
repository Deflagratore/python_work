my_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', 'sushi']
friend_food = my_food[:]

friend_food.append('chocolate')
my_food.append('kebab')

print(f"My favorite foods are:{my_food}")
print(f"My friend's favorite foods are:{friend_food}")

print(f"My three favorite foods are: {my_food[:3]}")
print(f"My least favorite foods are: {my_food[-3:]}")