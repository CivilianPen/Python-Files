put = 0
p = -1
stek = []
put = input()
while put != "exit":
    p=put.find("push")
    probel=put.find(" ")
    if len(stek) == 0 and (put == "front" or put == "pop"):
        print("error")
    if p>=0:
        stek.append(put[probel+1:])
        print("ok")
        p = -1
    if put == "pop" and len(stek) > 0:
        print(stek[0])
        stek = stek[1:]
    if put == "front" and len(stek) > 0:
        print(stek[0])
    if put == "size":
        print(len(stek))
    if put == "clear":
        stek = []
        print("ok") 
    put = input()
print("bye")
