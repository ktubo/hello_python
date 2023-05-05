def remov_nb(n):
    original_array = []
    temp_array = original_array
    prod = 0

    for i in range(1, n+1):
        original_array.append(i)

    for i in original_array[:-1]:
        temp_array.remove(i)
        for x in temp_array:
            prod *= i
            if prod == sum(original_array) - (prod+i):
                return True
            else:
                return False
            prod = 0


num = 5
print(remov_nb(num))
