def merge_sort(string: str):
    if len(string) <= 1:
        return string

    mid = len(string) // 2

    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left == []:
        result += right
    else:
        result += left

    return result


def is_anagram(first_string, second_string):
    first = merge_sort(first_string)
    second = merge_sort(second_string)

    if first == second:
        return (first, second, True)

    else:
        return (first, second, False)
