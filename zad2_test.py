#map func
duzina_stranice=[1,2,3,4,5,6]

povrsine_kvadrata=[]
for i in duzina_stranice:
    povrsina=i**2
    povrsine_kvadrata.append(povrsina)
print(povrsine_kvadrata)


#filter func
list_animals=[]
animals = ['', 'cat', 'mouse', '', 'dog']
for i in animals:
    if i!='':
        list_animals.append(i)
print(list_animals)

#reduce func
sum=1
numbers = [1,2,3,4,5,6,7]
for i in numbers:
    sum = sum*i
print(sum)
