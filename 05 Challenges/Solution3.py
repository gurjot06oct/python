import random
def matrices_generator(n):
    original_matrix = [[random.randint(1,n*n) for  j in range(n)] for  i in range(n)]
    print(original_matrix)
    def check(i,j,v):
        return original_matrix[i][j] == v

    def permutations_fun(my_list):
        if len(my_list) <= 1:
            return [my_list]
        else:
            result = []
            for i in range(len(my_list)):
                first_element = my_list[i]
                remaining_elements = my_list[:i] + my_list[i+1:]
                for perm in permutations_fun(remaining_elements):
                    result.append([first_element] + perm)
            return result
    permutations=permutations_fun(list(range(n)))
    def transformed_matrix():
        n_list=permutations[random.randint(0,len(permutations)-1)]
        return [[original_matrix[i][j] for  j in n_list] for  i in n_list]

    return check,permutations,transformed_matrix()
n= int(input())
check,permutations,transformed_matrix= matrices_generator(n)
recombination =  [[j for j in range(n)] for i in range(n)]
equal= False
for permutation in permutations:
    for i in range(n):
        for j in range(n):
            if not check(permutation[i],permutation[j],transformed_matrix[i][j]):
                equal = False
                break
            recombination[permutation[i]][permutation[j]]=transformed_matrix[i][j]
            equal=True
        if not equal:
            break
    if equal:
        print(transformed_matrix,recombination,sep="\n")
        break