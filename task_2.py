def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None:
        return (iterations, "No upper bound found")
    return (iterations, upper_bound)

# Відсортований масив з дробовими числами
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]

# Число для пошуку
target = 5.5

# Тестування функції
print(binary_search(arr, target))  # Приклад використання, який можна протестувати

# Число, якого немає в масиві, але має бути верхня межа
target_missing = 5.0
print(binary_search(arr, target_missing))  # Повинно повернути кількість ітерацій та найближчий більший елемент
