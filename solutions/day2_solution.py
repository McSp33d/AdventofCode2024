from utils import *

reports=readIntLists("../input/day2_input")

def is_safe(report):
    if not report: return False
    if len(report)<=1: return True
    increasing = report[0]<report[1]
    for i in range(1,len(report)):
        if report[i-1]<report[i] and not increasing:
            return False
        if report[i-1]>report[i] and increasing:
            return False
        if abs(report[i-1]-report[i])>3 or abs(report[i-1]-report[i])==0:
            return False
    return True

def canBeFixed(report):
    report_copies=[report[:] for i in range(len(report))]
    for i, copied_report in enumerate(report_copies):
        copied_report.pop(i)
        if is_safe(copied_report):
            return True
    return False

def sol1():
    c=0
    for report in reports:
        if is_safe(report):
            c+=1
    return c

def sol2():
    c=0
    for report in reports:
        if is_safe(report) or canBeFixed(report):
            c+=1
    return c

if __name__=="__main__":
    print(sol1())
    print(sol2())