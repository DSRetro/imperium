from imperium.util import getFile

def getVersion():
    with open(getFile("VERSION"), "r") as file:
        data = str(file.read()).split("\\n")[0]
    return data
