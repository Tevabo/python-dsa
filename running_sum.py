def running_sum(nums):
    answer = []
    total = 0

    for i in nums:
        total += i
        answer.append(total)
    print(answer)
    return answer


list = [1, 2, 3, 4, 5]

running_sum(list)
