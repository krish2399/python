# point = {"x": 1, "y": 2}
point = dict(x=10, y=2)
point["x"] = 20
point["z"] = 40
print(point)

if "a" in point:
    print(point["a"])

print(point.get("a", "key was not found"))

del point["x"]
print(point)
print("\n")

for key in point.items():
    print(key)
