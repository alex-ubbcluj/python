def key_is_none(key):
    return key


def my_sorted(lst, key=None, reverse=False) -> list:
    """
    Functie proprie de sortare pe baza de merge sort
    param. lst: lista de sortat
    param. key (optional): functia dupa care se va sorta lista
    param. reverse (optional): False pentru sortare crescatoare,
                               True pentru sortare descrescatoare
                               default: False
    return: lista sortata corespunzator
    """
    if key is None:
        key = key_is_none

    if reverse is False:
        if len(lst) > 1:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]

            my_sorted(left, key, reverse)
            my_sorted(right, key, reverse)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if key(left[i]) <= key(right[j]):
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

        return lst
    else:
        if len(lst) > 1:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]

            my_sorted(left, key, reverse)
            my_sorted(right, key, reverse)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if key(left[i]) >= key(right[j]):
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

        return lst
