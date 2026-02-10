from pathlib import Path

path = Path("ecommerce")
# # print(path.exists())
# # path.mkdir()
# # path.rmdir()
# # path.rename("ecommerce_new")

print(path.iterdir())

for p in path.iterdir():
    print(p)

# # path = [p for p in path.iterdir()]
# # print(path)
