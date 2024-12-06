from utils import *

data_ordering=read("../input/day5_input1.txt")

#key smaller than value
page_order={}

for line in data_ordering:
    num1, num2= line.split("|")
    num1=int(num1)
    num2=int(num2)
    if num1 in page_order:
        page_order[num1].append(num2)
    else:
        page_order[num1]=[num2]

def is_in_order(page1, page2):
    if page1 in page_order and page2 in page_order[page1]:
        return True
    if page2 in page_order and page1 in page_order[page2]:
        return False
    return True

given_updates=readIntLists("../input/day5_input2.txt", ",")

#categorize updates
correct_updates=[]
incorrect_updates=[]
for update in given_updates:
    update_in_correct_order=True
    for i, page1 in enumerate(update):
        for j in range(i+1, len(update)):
            page2=update[j]
            if not is_in_order(page1, page2):
                update_in_correct_order=False
                break
        if not update_in_correct_order:
            break
    if update_in_correct_order:
        correct_updates.append(update)
    else:
        incorrect_updates.append(update)

def sort_update(update):
    #base case
    if len(update)==1:
        return update
    #find smallest value
    prev_value=update[0]
    for value in update:
        if not is_in_order(prev_value, value):
            prev_value=value
    #recursion part
    update.pop(update.index(prev_value))
    return [prev_value]+sort_update(update)

def sol1():
    c=0
    for update in correct_updates:
        mid=len(update)//2
        c+=update[mid]
    return c

def sol2():
    c=0
    for update in incorrect_updates:
        mid=len(update)//2
        sorted_update=sort_update(update)
        c+=sorted_update[mid]
    return c

print(f"Solution1: {sol1()}")
print(f"Solution2: {sol2()}")
