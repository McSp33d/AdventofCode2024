from utils import *

data_ordering=read("../input/day5_input1.txt")

#key smaller than value
order={}

for line in data_ordering:
    num1, num2= line.split("|")
    num1=int(num1)
    num2=int(num2)
    if num1 in order:
        order[num1].append(num2)
    else:
        order[num1]=[num2]

def is_in_order(num1, num2):
    if num1 in order and num2 in order[num1]:
        return True
    if num2 in order and num1 in order[num2]:
        return False
    return True

proposed_orderings=readIntLists("../input/day5_input2.txt", ",")

correct_order=[]
incorrect_order=[]
for proposed_ordering in proposed_orderings:
    ordering_correct=True
    for i in range(len(proposed_ordering)):
        num1=proposed_ordering[i]
        for j in range(i+1, len(proposed_ordering)):
            num2=proposed_ordering[j]
            if not is_in_order(num1, num2):
                ordering_correct=False
                break
        if not ordering_correct:
            break
    if ordering_correct:
        correct_order.append(proposed_ordering)
    else:
        incorrect_order.append(proposed_ordering)

def sort_ordering(ordering):
    if len(ordering)==1:
        return ordering
    #find smallest value
    prev_value=ordering[0]
    for value in ordering:
        if not is_in_order(prev_value, value):
            prev_value=value
    #recursion part
    ordering.pop(ordering.index(prev_value))
    return [prev_value]+sort_ordering(ordering)

def sol1():
    c=0
    for o in correct_order:
        mid=len(o)//2
        c+=o[mid]
    return c

def sol2():
    c=0
    for o in incorrect_order:
        mid=len(o)//2
        original_length=len(o)
        new_ordering=sort_ordering(o)
        c+=new_ordering[mid]
    return c

print(f"Solution1: {sol1()}")
print(f"Solution2: {sol2()}")
