try:
    a = int(input("Enter an integer in the range [1, 10]: "))
    if a < 1 or a > 10:
        raise ValueError("Please follow the instructions.")
    else:
        raise Exception("a","b","c","d")
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Error Arguments:", e.args)
else:
    print("Else block is executed when try is succesful.")
finally:
    # finally block always run no matter what
    print("The End")

# Example of finally
def foo():
    try: 
        return 1
    finally:
        return 2
print(foo()) # 2