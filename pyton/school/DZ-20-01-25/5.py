nums = [2**m*3**n for m in range(0,30,2) for n in range(1,30,2) if 400000000 <= 2**m*3**n <=  600000000]
for n in sorted(nums):
    print(n)