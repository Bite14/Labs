numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


none_index = numbers.index(None)
numbers1 = numbers[:none_index]
numbers2 = numbers[none_index+1:]
sum_of_numbers = sum(numbers1) + sum(numbers2)
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers/count_of_numbers
numbers[none_index] = average_of_numbers


print("Измененный список:", numbers)
