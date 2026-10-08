def bubble_sort(a):
    n = len(a)

    for p in range(n - 1):
        swapped = False

        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if not swapped:
            break

    return a


numbers = [5, 2, 8, 1, 3]

print("Before sorting:", numbers)

bubble_sort(numbers)

print("After sorting:", numbers)