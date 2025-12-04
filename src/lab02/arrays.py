def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if len(nums) == 0:
        raise ValueError

    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:

    if len(nums) == 0:
        return []

    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:

    res = []

    for element in mat:
        if isinstance(element, list) or isinstance(element, tuple):
            for inner_element in element:
                res.append(inner_element)
        else:
            raise TypeError

    return res


print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
