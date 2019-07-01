from random import randint
l1 =  [randint(0, 9) for _ in range(100)]
l2 =  [randint(0, 9) for _ in range(100)]
l3 =  [randint(0, 9) for _ in range(100)]

idcs = sorted(range(len(l1)), key=lambda x: l1[x])
print(sorted(l1) == [l1[idx] for idx in idcs])

s1, s2, s3 = zip(*sorted(zip(l1,l2,l3)))
print(s1==sorted(l1))

