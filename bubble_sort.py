import random


def bubble_sort(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

if __name__ == '__main__':
    tamano_de_list = int(input('What will be the size of the list? '))

    list = [random.randint(0, 100) for i in range(tamano_de_list)]
    print(list)

    sorted_list = bubble_sort(list)
    print(sorted_list)
