from collections import Counter
numbers = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

counts = dict(Counter(numbers))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)