# Case conditions can only evaluate numeric values, iterables,None
# When evaluating iterables, only the order of values is considered, while the type of iterable is ignored.
# It's important to note that sets cannot be used in case conditions; they are an exception to this rule.

e = eval(input("enter anything :"))
match e:
    case [1, 2, 3]:
        print('list')
    case None:
        print('None')
    case {"a":"1323234"}:
        print("dict")
    # case {1,2,3}:
    #     print("set")
    case bool(1):
        print('bool')
    case default:
        # if no case matches
        print('none')