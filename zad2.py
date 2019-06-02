from functools import reduce

print('------------------------------------------------------')
print('map - area x^2')
# map
duzina_stranice = (1, 2, 3, 4, 5, 6)
print(duzina_stranice)
povrsina_lambda = lambda x: x*x
pov_kv_map = map(povrsina_lambda, duzina_stranice)
print(list(pov_kv_map))

# map pomocu for petlje


def my_map(povrsina_lambda, duzina_stranice):
    povrsine_kvadrata = []
    for i in duzina_stranice:
        povrsina = povrsina_lambda(i)
        povrsine_kvadrata.append(povrsina)
    return povrsine_kvadrata

print(my_map(povrsina_lambda, duzina_stranice))

print('------------------------------------------------------')
print('filter - "" out empty strings')
filter_lambda = lambda x: x != ''
animals = ['', 'cat', 'mouse', '', 'dog']
print(animals)
animals_filter = filter(filter_lambda, animals)
print(list(animals_filter))

# filter for petlja


def filter_animals(filter_lambda, animals):
    list_animals = []
    for i in animals:
        if filter_lambda(i):
            list_animals.append(i)
    return list_animals
print(filter_animals(filter_lambda, animals))


print('------------------------------------------------------')
print('reduce - sum x^3')
# reduce
numbers = [10, 2, 3, 4, 5, 6]
print(numbers)
sum_prod_lambda = lambda x: x**3

reduce_calc = reduce((lambda x, y: x+y**3), [0]+numbers)
print(reduce_calc)


def reduce_numbers(sum_prod_lambda, numbers):
    sum = 0
    for i in numbers:
        sum += sum_prod_lambda(i)
    return sum
print(reduce_numbers(sum_prod_lambda, numbers))
