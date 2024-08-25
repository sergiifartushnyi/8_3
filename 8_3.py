from collections import Counter

def find_unique_value(numbers):

    count = Counter(numbers)

    for number, freq in count.items():
        if freq == 1:
            return number

    return None

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
print("ОК")