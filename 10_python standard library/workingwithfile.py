from pathlib import Path
from time import ctime
import shutil


# path = Path(r"D:\Python\10_python standard library\ecommerce\__init__.py")
# print(path.exists())

# (path/"__init__.py").touch()#for add file
# path.rename("init.txt")#for rename
# path.unlink("init.txt") #for delete

# print(ctime(path.stat().st_birthtime))#cration time of file

# with open("__init__.py", "r") as file:
#     ...


# print(path.read_bytes())
# print(path.read_text()) 


# path.write_text("print('Jay Shree Krishna')")
# path.write_bytes(b"print('Har Har Mahadev')")


source =  Path(r"D:\Python\10_python standard library\ecommerce\__init__.py")
target = Path() / "__init__.py"

# shutil.copy(source,target)
target.write_text(source.read_text())