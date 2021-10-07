def insertion_sort(numbers):

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]
            j = j - 1
        
        numbers[j+1] = key
    
    print(numbers)

insertion_sort([9, 0, 18, 21, 8, 1])

