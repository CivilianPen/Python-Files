from itertools import product
gl = ['и', 'е', 'о', 'а']
sgl = ['г', 'п', 'р', 'б', 'л']
arr = product('гипербола', repeat = 6)
fin = []
count = 0

for i in arr:
  count += 1
  l = "".join(i)
  K = False
  if l[0] in sgl and  l[5] in sgl:
    if (l[1] in gl and l[2] in sgl) or (l[2] in gl and l[1] in sgl and l[3] in sgl) or (l[3] in gl and l[2] in sgl and l[4] in sgl) or (l[4] in gl and l[3] in sgl) :
      pass
    else:
      fin.append(l)

print(len(fin))

      
