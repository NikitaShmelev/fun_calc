from random import randint
from main import calc_task

def get_random_lines():
    line_for_eval = ''
    line_for_calc = ''
    operations = ['^', '/', '*', '-', '+']

    def get_digit(line_for_eval, line_for_calc):
        if randint(0, 1):
                # type of digit (float(1) or int(0))
                item = round(randint(1, 100)/randint(1, 100), 2)
                line_for_eval += str(item)
                line_for_calc += str(item)
        else:
            item = randint(1, 100)
            line_for_eval += str(item)
            line_for_calc += str(item)
        return line_for_eval, line_for_calc

    # if randint(0, 1):
    #     line_for_eval += '-'
    #     line_for_calc += '-'
    line_for_eval, line_for_calc = get_digit(line_for_eval, line_for_calc)

    count_of_iteration = 10
    for i in range(count_of_iteration):
        if i != count_of_iteration:
            
            rand_digit = randint(0, 4)
            if rand_digit == 0:
                # power
                line_for_eval += '**'
                line_for_calc += '^'
            else:
                line_for_eval += operations[rand_digit]
                line_for_calc += operations[rand_digit]
            line_for_eval, line_for_calc = get_digit(line_for_eval, line_for_calc)
        else:
            line_for_eval, line_for_calc = get_digit(line_for_eval, line_for_calc)
    return line_for_eval, line_for_calc 
count_of_iteration = 100
correct = 0
for i in range(1, count_of_iteration+1):
    line_for_eval, line_for_calc = get_random_lines()
    
    try:
        res_eval = eval(line_for_eval)
        res_calc = calc_task(line_for_calc)
        if res_eval == res_calc[0]:
            correct += 1
            print(f'Test {i}, sukces {correct*100/count_of_iteration}%')
    except:
        print(f'Test {i}, failed')