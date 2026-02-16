from pathlib import Path

path = Path(r"D:\Python\10_python standard library\ecommerce\__init__.py")
print(path.exists())
print(path.home())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_suffix(".txt")
print(path)