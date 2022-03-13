def calc(operation, a, b):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '^':
        return a**b
    else:
        return a/b if b != 0 else False

def stlitter(line):
    res = list()
    check_index = None
    if line[0] == '-':
        sub_res = line[0]
        for i in enumerate(line[1:]):
            try:
                if i[1] != '.':
                    float(i[1])
            except ValueError:
                sub_res += line[1:i[0]+1]
                line = line[i[0]+1:]
                res.append(sub_res)
                break
    for i in enumerate(line):
        if i[1] in ["+", "-", "^", "/", "*"]:
            if check_index == None:
                res.append(line[0:i[0]])
            else:
                res.append(line[check_index+1:i[0]])
            res.append(line[i[0]])
            check_index = i[0]
    else:
        res.append(line[check_index+1:])
        if '' in res:
            res.remove('')
    return res
