# calling fruitless function and returning value in list comprehension
def fruitless(x):
    print(x)
    # It can return anything true, false, none etc
    return True
listing =  [1,2,3,4,5,6,7]
listing2 = [str(type(fruitless(i))) and i  for i in listing ]
listing3 = [(fruitless(i) or True) and i  for i in listing ]
print(listing2,listing3)