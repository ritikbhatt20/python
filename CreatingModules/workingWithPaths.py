from pathlib import Path

path = Path("ecommerce/__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)