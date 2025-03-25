s = input()
fit = {')':'(', '}':'{', ']':'['}
st = []

res = 'yes'
for a in s:
    try:
        if a in '({[':
            st.append(a)
        elif a in ')}]':
            if fit[a]!=st.pop():
                res = 'no'
            break
    except:
        res = 'no'
        break

if st:
    res = 'no'

print(res)
