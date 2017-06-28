import os
def get_size(start_path = ""):
    total_size = 0
    for dirs in os.listdir(start_path):
        for dirpath, dirnames, filenames in os.walk("{0}/{1}".format(start_path, dirs)):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        print("{0} = {1}kb".format(dirs, total_size/1000))
        total_size = 0
    return True

import zipfile
zip_ref = zipfile.ZipFile("", 'r')
zip_ref.extractall("")
zip_ref.close()

for dirpath, dirnames, filenames in os.walk(""):
    for f in filenames:
        if f.endswith(".pak"):
            print(f)
