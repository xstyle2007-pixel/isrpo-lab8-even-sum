def sum_even_numbers(numbers):
    """
    Возвращает сумму всех чётных чисел в массиве.
    Если чётных чисел нет — возвращает 0.
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Ожидается список или кортеж целых чисел")

    total = 0
    for x in numbers:
        if not isinstance(x, int) or isinstance(x, bool):
            raise TypeError(f"Элемент {x!r} не является целым числом")
        if x % 2 == 0:
            total += x
    return total

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 12),
        ([1, 3, 5], 0),
        ([], 0),
        ([-2, -4, -6], -12),
        ([0, 1, 2], 2),
    ]
    for arr, expected in test_cases:
        result = sum_even_numbers(arr)
        print(f"{arr} -> {result} (ожидалось {expected})")
