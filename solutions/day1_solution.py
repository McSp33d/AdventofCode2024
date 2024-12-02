from utils import *

def sol1():
    data=[_.split("   ") for _ in read("../input/day1_input")]
    nums1=sorted([int(i[0]) for i in data])
    nums2=sorted([int(i[1]) for i in data])
    total_distance=0
    for i, j in zip(nums1, nums2):
        total_distance+=abs(i-j)
    return total_distance


def sol2():
    data=[_.split("   ") for _ in read("../input/day1_input")]
    left_list=sorted([int(i[0]) for i in data])
    right_list=sorted([int(i[1]) for i in data])
    similarity_score=0
    for n in left_list:
        similarity_score+=right_list.count(n)*n
    return similarity_score

print("Solution 1:", sol1())
print("Solution 2:", sol2())