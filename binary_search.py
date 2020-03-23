import random

def binary_search(list, start, end, target):
    print('----------------------------------------------')
    print(f'Start {start}')
    print(f'End {end}')

    # print(f'Searching {target} between {list[start]} and {list[end - 1]}')
    if start > end:
        return False

    if target > list[end-1]:
        return False

    middle = (start + end) // 2
    print(f'Middle {middle}')
    print(f'Element in middle {list[middle]}')
    print(f'Target {target}')

    if list[middle] == target:
        return True
    elif list[middle] < target:
        return binary_search(list, middle + 1, end, target)
    else:
        return binary_search(list, start, middle - 1, target)


if __name__ == '__main__':
    list_size = int(input('What will be the size of the list? '))
    target    = int(input('What number do you want to find? '))

    list   = sorted([random.randint(0, 100) for i in range(list_size)])

    result = binary_search(list, 0, len(list), target)

    print(list)
    print(f'Element {target} {"is" if result else "is not"} in the list')
