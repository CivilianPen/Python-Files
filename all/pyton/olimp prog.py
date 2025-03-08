put = input()
stack = [] 
for el in put: 
    if el in ["(", "{", "["]: 
        stack.append(el) 
    else:  
        if not stack:
            break
            print('no')
        current_el = stack.pop() 
        if current_el == '(': 
            if el != ")":
                break
                print('no')
        if current_el == '{': 
            if el != "}": 
                break
                print('no')  
        if current_el == '[': 
            if el != "]":
                break
                print('no')
print('yes')
