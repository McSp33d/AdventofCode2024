from utils import *
import re

data = "".join(read("../input/day3_input"))

def mul(expression):
    a,b = expression[4:-1].split(",")
    return int(a)*int(b)

def sol1(calculation):
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    output=0
    for m in re.findall(pattern, calculation):
        output+=mul(m)
    return output

def sol2(calculation):
    dos_matches=re.finditer(r"do\(\)", calculation)
    donts_matches=re.finditer(r"don't\(\)", calculation)
    dos=[match.start() for match in dos_matches]
    donts=[match.start() for match in donts_matches]
    indices=[[0, "do"]]+[[i, "do"] for i in dos]+[[i, "dont"] for i in donts]+[[len(calculation), "do"]]
    indices.sort()
    new_calculation=""

    for i, instruction in enumerate(indices[:-1]):
        if instruction[1]=="do":
            new_calculation+=calculation[instruction[0]:indices[i+1][0]]

    return sol1(new_calculation)

print(f"solution1: {sol1(data)}")
print(f"solution2: {sol2(data)}")

text = "do() some text don't() and another do() more text do() and then do()"

# Pattern to match from do() to don't() or do(), using lookahead
pattern = r"do\(\).*(?=don't\(\)|do\(\))"

# Find all matches
matches = re.findall(pattern, text)

print(matches)
