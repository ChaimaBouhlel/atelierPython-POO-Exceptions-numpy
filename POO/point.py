class Point:
	"Definition d'un point geometrique"

a = Point()
a.x = 1
a.y = 2
b = Point()
b.x = 3
b.y = 4
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)

b = a
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)

a.x = 3
a.y = 4
print("a : x =", a.x, "y =", a.y)
print("b : x =", b.x, "y =", b.y)
