tuple1= () #tuple
tuple2 = (1,)  #tuple
tuple3= (1)  #int

tup = (0,1,2,3,4,5,6,7,8,9)
print(tup)

#creating new tuple with list comprehension
tup2 =  tuple(i*i for i in tup)
print(tup2)



tup3 = (i*i for i in tup)
tup4 = (i*i for i in tup)
# type(tup3) -> generator

# access in generator
# ---method 1 ---
print("tup3",*tup3)
print("tup3",*tup3) # will be empty as it is a generator
# ---method 2 ---
for i in tup4:
    print(i)




#accesing elements
# by index
print(tup[1])   #1

# by iteration
for i in tup:
    print(i)

# Count elements
print(tup.count(1))

# Find indexof
# .index(value,[start,[stop]])
print(tup.index(5))