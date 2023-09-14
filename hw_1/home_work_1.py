# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

numbers = [2, 18, 8, 34, 122, 0, -7, 31, 89, -25]

def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

print(sort_list_imperative(numbers))

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

nums = [2, 18, 8, 34, 122, 0, -7, 31, 89, -25]

def sort_list_declarative(nums):
    nums.sort(reverse = True)
    return nums

print(sort_list_declarative(nums))