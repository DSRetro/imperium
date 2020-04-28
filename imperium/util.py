import os

def getFile(rel_dir):
    return str(os.path.join(os.path.split(__file__)[0], rel_dir.replace("/", "\\")))
