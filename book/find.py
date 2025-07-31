import os

root = r'/path/to/your/dir'
files = [name for name in os.listdir(root)
                  if os.path.isfile(os.path.join(root, name))]
print(files)

