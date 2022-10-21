import os
try:
    directory="Rohanp"
    store_dir="D:/"
    path = os.path.join(store_dir,directory)
    os.mkdir(path)
    print("directory %s is created",directory)
except OSError as error:
    print("the folder doesn't exist %s"% error)