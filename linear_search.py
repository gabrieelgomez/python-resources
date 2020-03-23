import random

def linear_search(list, target):
    match = False

    for element in list: # This is O(n), Linear Search Algorithmic
        if element == target:
            match = True
            break

    return match


if __name__ == '__main__':
    list_size = int(input('What will be the size of the list? '))
    target    = int(input('What number do you want to find? '))

    list      = [random.randint(0, 100) for i in range(list_size)]

    result    = linear_search(list, target)

    print(list)
    print(f'Element {target} {"is" if result else "is not"} in the list')
