from typing import List


def swap(n: List[int]) -> List[int]:
    n[0] += n[1]
    n[1] = n[0] - n[1]
    n[0] -= n[1]

    return n


print(swap([3, 4]))
