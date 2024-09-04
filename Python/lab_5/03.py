fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'egg')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index]

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

del food_stuff_tp

print("Food stuff list:", food_stuff_lt)
print("Middle items:", middle_items)
print("First three items:", first_three)
print("Last three items:", last_three)
