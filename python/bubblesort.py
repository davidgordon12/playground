from typing import List


def sort(n: List[int]) -> List[int]:
    for i in range(len(n)-1):
        for j in range(len(n) - 1 - i):
            if n[j] > n[j+1]:
                n[j] += n[j+1]
                n[j+1] = n[j] - n[j+1]
                n[j] -= n[j+1]
    return n


print(sort([1, 3, 7, 2, 4, 9, 1]))
