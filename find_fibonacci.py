lst = [0, 1]

def find_fibonacci(limit):
    if limit == 1:
        print(lst[0])
    elif limit == 2:
        print(','.join(map(str, lst)))
    else:
        for i in range(3,limit+1):
            length = len(lst)
            second_last_number = length - 2
            lst.append(lst[-1] + lst[second_last_number])

        print(','.join(map(str, lst)))
        

find_fibonacci(8)
