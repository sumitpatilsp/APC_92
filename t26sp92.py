t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)

common = tuple(set(t1) & set(t2))

print("Common elements:", common)