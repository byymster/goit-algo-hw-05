def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо верхню межу не знайдено під час пошуку, визначаємо її після завершення циклу
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)

# Приклад використання
arr = [0.1, 0.5, 1.3, 2.7, 3.8, 4.2, 5.9]
target = 2.5
result = binary_search(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}") # Виведе: Кількість ітерацій: 3, Верхня межа: 2.7