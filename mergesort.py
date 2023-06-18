def merge_sort(lst):
    """
    Sortiert eine Liste mit dem Merge-Sort-Algorithmus.

    Args:
        lst (list): Die zu sortierende Liste.

    Returns:
        None (Die Sortierung erfolgt direkt auf der übergebenen Liste.)

    """
    if len(lst) <= 1:
        return

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def plot_data(data):
    x = range(len(data))
    plt.figure(figsize=(8, 6))
    plt.plot(x, data, marker='o', linestyle='-', color='blue')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Merge Sort')
    plt.grid(True)
    plt.show()

def mergeSort(list_to_sort_by_merge):
    # Implementierung des Merge-Sort-Algorithmus hier

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot_data(my_list)
mergeSort(my_list)
plot_data(my_list)

