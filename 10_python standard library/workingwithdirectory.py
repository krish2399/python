from pathlib import Path

path = Path(r"D:\Python\10_python standard library\ecommerce")
# print(path.exists("Krish"))


 #make a directory
# Path.mkdir("Krish")

    #delete a directory
# path = Path("Krish")
# path.rmdir()


    #rename directory
# path.rename("ecommerce2")


# print(path.iterdir())

# for p in path.iterdir():
#     print(p)


# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

py_file = [p for p in path.rglob("*.py")]
print(py_file)