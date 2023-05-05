"""
From CodeWars: Pete, the Baker
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

"""


def cakes(recipe, available):
    num_of_cakes = 0
    num_of_ingredients = 0

    for i in recipe:
        if i in available:
            if available[i] >= recipe[i]:
                # number of cakes that can be baked for this iteration
                temp_num_of_cakes = available[i] // recipe[i]
                # counts number of ingredients used in the recipe
                num_of_ingredients += 1
                if num_of_cakes == 0 or num_of_cakes > temp_num_of_cakes:
                    # number is replaced with least amount of cakes that can be baked
                    num_of_cakes = temp_num_of_cakes

    # compares whether number of ingredients used is same as recipe
    if num_of_ingredients == len(recipe):
        return num_of_cakes
    else:
        num_of_cakes = 0
        return num_of_cakes


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"sugar": 1200, "flour": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe,available))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"sugar": 1, "flour": 1, "eggs": 5, "milk": 200}
print(cakes(recipe,available))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {}
print(cakes(recipe,available))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"milk": 200}
print(cakes(recipe,available))

recipe = {"eggs": 5}
available = {"sugar": 1200, "flour": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe,available))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"sugar": 1200, "flour": 5000, "eggs": 9, "milk": 200}
print(cakes(recipe,available))


"""
# Another solution:

def cakes(recipe, available):
    list = []
    for ingredient in recipe:
        if ingredient in available:
            list.append(available[ingredient]/recipe[ingredient])
        else:
            return 0
    return min(list)
"""