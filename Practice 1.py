def cube_dict_odd_numbers(input_list):
    return {x: x**3 for x in input_list if x % 2 != 0}

def even_unique_numbers(input_list):
    return {x for x in input_list if x % 2 == 0}

def exclude_list(input_list, excluded_list):
    return [x for x in input_list if x not in excluded_list]

def divisible_by_seven_generator(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i

list_1 = [1,2,3,4,5,6,7]
result_dict = cube_dict_odd_numbers(list_1)
print(result_dict)

list_2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
result_set = even_unique_numbers(list_2)
print(result_set) 

list_3 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
excluded_list = list_3
result_list = exclude_list(list_3, excluded_list)
print(result_list) 

n = 50
for num in divisible_by_seven_generator(n):
    print(num)
