def merge_sort(string: str):
    if len(string) <= 1:
        return string

    mid = len(string) // 2

    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])

    return merge(left, right)


def merge(left: str, right: str):
    result = ''

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result += left[0]
            left = left[1:]
        else:
            result += right[0]
            right = right[1:]

    if left == '':
        result += right
    else:
        result += left

    return result


def is_anagram(first_string, second_string):
    first = merge_sort(first_string.lower())
    second = merge_sort(second_string.lower())

    if first == '' or second == '':
        return (first, second, False)

    if first == second:
        return (first, second, True)

    else:
        return (first, second, False)
