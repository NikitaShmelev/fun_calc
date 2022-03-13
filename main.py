from math import *
from funcs import calc, stlitter

line = "-2+2*9*2^2"
# print(line)



def calc_task(line):
    array = stlitter(line)
    operations = ['^', '/', '*', '-', '+']
    check_index = 0
    while True:
        try:
            operation_id = array.index(operations[check_index])
        except ValueError:
            if check_index < len(operations)-1:
                check_index += 1
                continue
            else:
                break
        sub_res = calc(
            operation=operations[check_index],
            a=float(array[operation_id-1]),
            b=float(array[operation_id+1])
            )
        if sub_res:
            array = array[0:operation_id-1] + [sub_res] + array[operation_id+2:]
        else:
            break
    return array
# print(calc_task())
