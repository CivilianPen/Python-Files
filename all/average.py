def get_average_by_summ(string):
    try:
        summa = eval(string)
        count = 0
        for i in string:
            if i.isdigit():
                count+=int(1)
        return summa/count
    except:
        return False

def get_average_by_list(string):
    try:
        arr = []
        for i in string:
            if i.isdigit():
                arr.append(int(i))
                
        return sum(arr)/len(arr)
    except:
        return False

while True:
    string = input()
    if "+" in string and (('*' in string)==False) and (('/' in string)==False) and (('-' in string)==False):
        if get_average_by_summ(string)!= False:
            print(get_average_by_summ(string))
        elif string == 'exit':
            break
    else:
        if get_average_by_list(string)!= False and (('*' in string)==False) and (('/' in string)==False) and (('-' in string)==False):
            print(get_average_by_list(string))
        elif string == 'exit':
            break
