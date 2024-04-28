def sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum(numbers[1:])


result_with_recursion = sum([1, 2, 3, 4])
print("Результат з рекурсією:", result_with_recursion)
