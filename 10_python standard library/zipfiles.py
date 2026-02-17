from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zipd", "w") as zip:
    for path in Path(r"D:\Python\10_python standard library\ecommerce").rglob("*.*"):
        zip.write(path)
