#sort and reverse sort dict
dict1={
    'name':'star',
    'year':2002,
    'fruit':'strawberry',
    'month':'april'

}
sorted_dict=dict(sorted(dict1.items()))

print("sorted:",sorted_dict)
print("reverse sorted:",dict(reversed(sorted(dict1.items()))))


#check if a key exists 
cat = {
    'name':'kitty',
    'color':'white',
    'breed': 'persian',
    'age':2
}
print("breed key exists in dict:", 'breed' in cat)

#merge two dictionaries
owner={
    'owner_name':'ella',
    'owner_age':22
}

cat.update(owner)
print(cat)

#add item to a tuple
tup1=("apple", "peach", "mango")
tup1= list(tup1)
tup1.append("strawberry")
tup1=tuple(tup1)
print(tup1)

#create tuple with different data types
tup2=("eyes", "nose", "lips")
tup3=(1,2,3)
tup4= tup2+tup3
print(tup4)

#sum items in a list
lst=[1,2,3,4,5]
sum=0
for i in lst:
    sum+=i
print(sum)

#print largest number in list
lst2=[31,2,4,9,87,56,22]
print(max(lst2))

#add member in a set
set1={1,2,5,4,3}
set1.add(6)
set1.update([78,21])
print(set1)

#reverse items in an array
lst3=[1,2,3,4,5]
lst3.reverse()
print(lst3)

#display array items 
lst4=[10,20,30,40,50]
print(lst4[0])
print(lst4[1])
print(lst4[2])
print(lst4[3])
print(lst4[4])