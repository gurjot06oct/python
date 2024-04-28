# calling fruitless function and returning value in list comprehension
def fruitless(x):
    print(x)
    return None
listing =  [1,2,3,4,5,6,7]
listing2= [fruitless(i) or i for i in listing ]
print(listing2)