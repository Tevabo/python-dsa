array1 = [1, 2, 4, 6, 8]
target1 = 8


def two_sum(numbers, target):
    values = dict()
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in values:
            return [values[complement], i]
        values[num] = i


two_sum(array1, target1)
