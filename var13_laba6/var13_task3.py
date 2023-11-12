def find_sum_between_positives(arr):
    first_positive_index = -1
    second_positive_index = -1
    total_sum = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            if first_positive_index == -1:
                first_positive_index = i
            elif second_positive_index == -1:
                second_positive_index = i
                break

    if first_positive_index != -1 and second_positive_index != -1:
        for j in range(first_positive_index + 1, second_positive_index):
            total_sum += arr[j]

    return total_sum

def move_zeros_to_end(arr):
    # Поиск первого нулевого элемента
    zeros_index = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros_index = i
            break

    # Перемещение нулевых элементов в конец списка
    if zeros_index != -1:
        for i in range(zeros_index + 1, len(arr)):
            if arr[i] != 0:
                arr[zeros_index] = arr[i]
                arr[i] = 0
                zeros_index += 1

    return arr

n = int(input("Введите размер списка: "))
arr = []
for _ in range(n):
    num = int(input("Введите число: "))
    arr.append(num)

print("Сумма элементов между первым и вторым положительными элементами:", find_sum_between_positives(arr))
print("Преобразованный список с нулями в конце:", move_zeros_to_end(arr))