k1 = (1, 2)
k2 = "test", 3
x1, x2 = 2, 3

print("k1", k1)
print("k2", k2)
print("x1 x2", x1, x2)

print("k1 len", k1, len(k1))

k3 = k1
print("k3", k3)

del k3
print("k1", k1)

print("k1[0]", k1[0])
#k1[0] = 3

k3 = k1 + k2
print("k3", k3)

k4 = k1 * 3
#k4 = k1 * k2
print("k4", k4)

k5 = (9,)
k6 = (8)
print("k5", k5)
print("k6", k6)
#print(k5 + k6)
print(k5 * k6)

k7 = k3[-2:]
print(k7)
