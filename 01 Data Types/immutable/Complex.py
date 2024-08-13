# creating varibales
complex1 = complex(1,4.6)
complex2 = complex(1+5j)
complex3 = complex("3+2j")
complex4 = 4+5j

print(complex1.conjugate())
print(complex1.imag) # float
print(complex1.real) # float

# complex has no default typecode but %s or %r can be used
print("%s".format(complex1))