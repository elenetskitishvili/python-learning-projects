def apply_operation(numbers, operation):
    return [operation(number) for number in numbers]


numbers = [1, 2, 3, 4, 5]

# Doubled
doubled = apply_operation(numbers, lambda number: number * 2)
print('Doubled:', doubled)

# Squared
squared = apply_operation(numbers, lambda number: number ** 2)
print('Squared:', squared)

# Filtered
filtered_items = apply_operation(
    numbers, lambda number: number if number % 2 == 1 else None)
filtered_odds = [item for item in filtered_items if item != None]
print('Filtered (odd numbers):', filtered_odds)


filtered_odds = list(filter(lambda number: number % 2 == 1, numbers))
print('Filtered (odd numbers):', filtered_odds)


filtered_odds = [number for number in numbers if number % 2 == 1]
print('Filtered (odd numbers):', filtered_odds)
