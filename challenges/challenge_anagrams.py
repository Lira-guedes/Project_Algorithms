def merge(left, right):
    response = []
    i_left = i_right = 0

    while i_left < len(left) and i_right < len(right):
        if left[i_left] < right[i_right]:
            response.append(left[i_left])
            i_left += 1
        else:
            response.append(right[i_right])
            i_right += 1

    response.extend(left[i_left:])
    response.extend(right[i_right:])
    return response


def sort_merge(value):
    if len(value) <= 1:
        return value
    mid = len(value) // 2

    return merge(sort_merge(value[:mid]), sort_merge(value[mid:]))


def is_anagram(first_string, second_string):
    def sort(value):
        return ''.join(sort_merge(value.lower()))

    first = sort(first_string)
    second = sort(second_string)

    if not first_string or not second_string:
        return (first, second, False)

    return (first, second, first == second)
